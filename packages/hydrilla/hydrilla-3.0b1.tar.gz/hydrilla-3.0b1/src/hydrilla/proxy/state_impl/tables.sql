-- SPDX-License-Identifier: GPL-3.0-or-later

-- SQLite tables definitions for Haketilo proxy.
--
-- This file is part of Hydrilla&Haketilo.
--
-- Copyright (C) 2022 Wojtek Kosior
--
-- This program is free software: you can redistribute it and/or modify
-- it under the terms of the GNU General Public License as published by
-- the Free Software Foundation, either version 3 of the License, or
-- (at your option) any later version.
--
-- This program is distributed in the hope that it will be useful,
-- but WITHOUT ANY WARRANTY; without even the implied warranty of
-- MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
-- GNU General Public License for more details.
--
-- You should have received a copy of the GNU General Public License
-- along with this program.  If not, see <https://www.gnu.org/licenses/>.
--
--
-- I, Wojtek Kosior, thereby promise not to sue for violation of this
-- file's license. Although I request that you do not make use of this
-- code in a proprietary program, I am not going to enforce this in
-- court.

BEGIN TRANSACTION;

CREATE TABLE general(
        haketilo_version      VARCHAR NOT NULL,
        default_allow_scripts BOOLEAN NOT NULL,
        advanced_user         BOOLEAN NOT NULL,
        repo_refresh_seconds  INTEGER NOT NULL,
        -- "mapping_use_mode" determines whether current mode is AUTO,
        -- WHEN_ENABLED or QUESTION.
        mapping_use_mode      CHAR(1) NOT NULL,

        CHECK (rowid = 1),
        CHECK (mapping_use_mode IN ('A', 'W', 'Q')),
        CHECK (haketilo_version = '3.0b1')
);

INSERT INTO general(
        rowid,
        haketilo_version,
        default_allow_scripts,
        advanced_user,
        repo_refresh_seconds,
        mapping_use_mode
)
VALUES(
        1,
        '3.0b1',
        FALSE,
        FALSE,
        24 * 60 * 60,
        'Q'
);

CREATE TABLE rules(
        rule_id       INTEGER PRIMARY KEY,

        pattern       VARCHAR NOT NULL,
        allow_scripts BOOLEAN NOT NULL,

        UNIQUE (pattern)
);

CREATE TABLE repos(
        repo_id             INTEGER PRIMARY KEY,

        name                VARCHAR NOT NULL,
        url                 VARCHAR NOT NULL,
        deleted             BOOLEAN NOT NULL DEFAULT FALSE,
        next_iteration      INTEGER NOT NULL DEFAULT 1,
        active_iteration_id INTEGER NULL,
        last_refreshed      INTEGER NULL,

        UNIQUE (name),
        -- The local semi-repo used for packages installed offline is always
        -- marked as deleted. Semi-repo's name is chosen as an empty string so
        -- as not to collide with other names (which are required to be
        -- non-empty).
        CHECK  ((repo_id = 1) = (name = '')),
        CHECK  (repo_id != 1 OR deleted = TRUE),
        -- All deleted repos shall have "url" set to an empty string. All other
        -- repos shall have a valid http(s) URL.
        CHECK  (deleted = (url = '')),
        -- Only non-deleted repos are allowed to have an active iteration.
        CHECK  (NOT deleted OR active_iteration_id IS NULL),
        -- Only non-deleted repos are allowed to have last refresh timestamp.
        CHECK  (NOT deleted OR last_refreshed IS NULL),

        FOREIGN KEY (active_iteration_id)
                REFERENCES repo_iterations(repo_iteration_id)
                ON DELETE SET NULL
);

INSERT INTO repos(repo_id, name, url, deleted)
VALUES(1, '', '', TRUE);

INSERT INTO repos(name, url)
VALUES('Hydrilla official', 'https://hydrilla.koszko.org/api_v2/');

CREATE TABLE repo_iterations(
        repo_iteration_id INTEGER PRIMARY KEY,

        repo_id           INTEGER NOT NULL,
        iteration         INTEGER NOT NULL,

        UNIQUE (repo_id, iteration),

        FOREIGN KEY (repo_id)
                 REFERENCES repos (repo_id)
);

CREATE VIEW orphan_iterations
AS
SELECT
        ri.repo_iteration_id,
        ri.repo_id,
        ri.iteration
FROM
             repo_iterations AS ri
        JOIN repos           AS r  USING (repo_id)
WHERE
        COALESCE(r.active_iteration_id != ri.repo_iteration_id, TRUE);

CREATE TABLE items(
        item_id         INTEGER PRIMARY KEY,

        -- "type" determines whether it's resource or mapping.
        type            CHAR(1) NOT NULL,
        identifier      VARCHAR NOT NULL,

        UNIQUE (type, identifier),
        CHECK  (type IN ('R', 'M'))
);

CREATE TABLE mapping_statuses(
        -- The item with this id shall be a mapping ("type" = 'M'). For each
        -- mapping row in "items" there must be an accompanying row in this
        -- table.
        item_id            INTEGER PRIMARY KEY,

        -- "enabled" determines whether mapping's status is ENABLED,
        -- DISABLED or NO_MARK.
        enabled            CHAR(1) NOT NULL DEFAULT 'N',
        -- "frozen" determines whether an enabled mapping is to be kept in its
        -- EXACT_VERSION, is to be updated only with versions from the same
        -- REPOSITORY or is NOT_FROZEN at all.
        frozen             CHAR(1) NULL,
        -- Only one version of a mapping is allowed to be active at any time.
        -- "active_version_id" indicates which version it is. Only a mapping
        -- version referenced by "active_version_id" is allowed to have rows
        -- in the "payloads" table reference it.
        -- "active_version_id" shall be updated every time dependency tree is
        -- recomputed.
        active_version_id  INTEGER NULL,

        CHECK (enabled IN ('E', 'D', 'N')),
        CHECK ((frozen IS NULL) = (enabled != 'E')),
        CHECK (frozen IS NULL OR frozen in ('E', 'R', 'N')),

        FOREIGN KEY (item_id)
                REFERENCES items (item_id)
                ON DELETE CASCADE,
        -- We'd like to set "active_version_id" to NULL when referenced entry is
        -- deleted, but we cannot do it with ON DELETE clause because the
        -- foreign key is composite. For now - this will be done by the
        -- application.
        FOREIGN KEY (active_version_id, item_id)
                REFERENCES item_versions (item_version_id, item_id)
);

CREATE TABLE item_versions(
        item_version_id     INTEGER  PRIMARY KEY,

        item_id             INTEGER  NOT NULL,
        version             VARCHAR  NOT NULL,
        -- "installed" determines whether item is INSTALLED, is NOT_INSTALLED or
        -- it FAILED_TO_INSTALL when last tried. If "required" in a row of
        -- "mapping_statuses is set to TRUE, the mapping version and all
        -- resource versions corresponding to it are supposed to have
        -- "installed" set to 'I'.
        installed           CHAR(1)  NOT NULL,
        repo_iteration_id   INTEGER  NOT NULL,
        definition          BLOB     NOT NULL,
        definition_sha256   CHAR(64) NOT NULL,
        -- "active" determines whether a version of this mapping is active
        -- because it is REQUIRED, has been AUTO activated or is NOT_ACTIVE.
        -- "active" shall be updated every time dependency tree is recomputed.
        -- It shall be set to NOT_ACTIVE if and only if given row does not
        -- correspond to "active_version_id" of any row in "mapping_statuses".
        active              CHAR(1)  NOT NULL DEFAULT 'N',

        UNIQUE (item_id, version, repo_iteration_id),
        -- Constraint below needed to allow foreign key from "mapping_statuses".
        UNIQUE (item_version_id, item_id),
        CHECK (installed in ('I', 'N', 'F')),
        CHECK (active in ('R', 'A', 'N')),

        FOREIGN KEY (item_id)
                REFERENCES items (item_id),
        FOREIGN KEY (repo_iteration_id)
                REFERENCES repo_iterations (repo_iteration_id)
);

CREATE VIEW repo_display_infos
AS
SELECT
        r.repo_id, r.name, r.url, r.deleted, r.last_refreshed,
        COALESCE(SUM(i.type = 'R'), 0) AS resource_count,
        COALESCE(SUM(i.type = 'M'), 0) AS mapping_count
FROM
                  repos           AS r
        LEFT JOIN repo_iterations AS ir USING (repo_id)
        LEFT JOIN item_versions   AS iv USING (repo_iteration_id)
        LEFT JOIN items           AS i  USING (item_id)
GROUP BY
        r.repo_id, r.name, r.url, r.deleted, r.last_refreshed;

-- Every time a repository gets refreshed or a mapping gets enabled/disabled,
-- the dependency tree is recomputed. In the process the "payloads" table gets
-- cleare and repopulated together with the "resolved_depended_resources" that
-- depends on it.
CREATE TABLE payloads(
        payload_id          INTEGER PRIMARY KEY,

        mapping_item_id     INTEGER NOT NULL,
        pattern             VARCHAR NOT NULL,
        -- What privileges should be granted on pages where this
        -- resource/mapping is used.
        eval_allowed        BOOLEAN NOT NULL,
        cors_bypass_allowed BOOLEAN NOT NULL,

        UNIQUE (mapping_item_id, pattern),

        FOREIGN KEY (mapping_item_id)
                REFERENCES item_versions (item_version_id)
                ON DELETE CASCADE
);

CREATE VIEW item_versions_extra
AS
SELECT
        iv.item_version_id,
        iv.item_id,
        iv.version,
        iv.installed,
        iv.repo_iteration_id,
        iv.definition,
        iv.active,
        r.repo_id, r.name AS repo,
        ri.repo_iteration_id, ri.iteration AS repo_iteration,
        COALESCE(r.active_iteration_id, -1) != ri.repo_iteration_id AND r.repo_id != 1
        AS is_orphan,
        r.repo_id = 1 AS is_local
FROM
                  item_versions    AS iv
        JOIN      repo_iterations  AS ri USING (repo_iteration_id)
        JOIN      repos            AS r  USING (repo_id);

CREATE TABLE resolved_depended_resources(
        payload_id       INTEGER,
        resource_item_id INTEGER,

        -- "idx" determines the ordering of resources.
        idx              INTEGER,

        PRIMARY KEY (payload_id, resource_item_id),

        FOREIGN KEY (payload_id)
                REFERENCES payloads (payload_id)
                ON DELETE CASCADE,
        FOREIGN KEY (resource_item_id)
                REFERENCES item_versions (item_version_id)
                ON DELETE CASCADE
) WITHOUT ROWID;

CREATE TABLE resolved_required_mappings(
        requiring_mapping_id INTEGER,
        required_mapping_id  INTEGER,

        PRIMARY KEY (requiring_mapping_id, required_mapping_id),

        FOREIGN KEY (requiring_mapping_id)
                REFERENCES item_versions (item_version_id)
                ON DELETE CASCADE,
        FOREIGN KEY (required_mapping_id)
                REFERENCES item_versions (item_version_id)
                ON DELETE CASCADE
) WITHOUT ROWID;

CREATE TABLE files(
        file_id INTEGER PRIMARY KEY,

        -- File's hash as hexadecimal string.
        sha256  CHAR(64) NOT NULL,
        -- The value of "data" - if not NULL - shall be a bytes sequence that
        -- corresponds the hash stored in "sha256".
        data    BLOB     NULL,

        UNIQUE (sha256)
);

CREATE TABLE file_uses(
        file_use_id     INTEGER PRIMARY KEY,

        -- If item version referenced by "item_version_id" has "installed" set
        -- to 'I', the file referenced by "file_id" is supposed to have "data"
        -- set to a valid, non-NULL value.
        item_version_id INTEGER NOT NULL,
        file_id         INTEGER NOT NULL,
        name            VARCHAR NOT NULL,
        -- "type" determines whether it's license file or web resource.
        type            CHAR(1) NOT NULL,
        mime_type       VARCHAR NOT NULL,
        -- "idx" determines the ordering of item's files of given type.
        idx             INTEGER NOT NULL,

        CHECK (type IN ('L', 'W')),
        UNIQUE(item_version_id, type, idx),
        UNIQUE(item_version_id, type, name),

        FOREIGN KEY (item_version_id)
                REFERENCES item_versions(item_version_id)
                ON DELETE CASCADE,
        FOREIGN KEY (file_id)
                REFERENCES files(file_id)
);

COMMIT TRANSACTION;
