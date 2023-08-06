;; SPDX-License-Identifier: CC0-1.0

;; Copyright (C) 2022 Wojtek Kosior <koszko@koszko.org>
;;
;; Available under the terms of Creative Commons Zero v1.0 Universal.

(define-module (hydrilla))

(use-modules
 (ice-9 rdelim)
 (ice-9 regex))

(define %source-dir (dirname (current-filename)))

;; The PKG-INFO file is generated when running `python3 -m build -s` or similar.
;; It is also automatically included in the generated tarballs.
(define %hydrilla-version
  (if (access? "src/hydrilla.egg-info/PKG-INFO" R_OK)
      (let* ((port (open-input-file "src/hydrilla.egg-info/PKG-INFO"))
             (process-line
              (lambda (self-ref)
                (let ((match-result
                       (string-match "^Version: (.*)" (read-line port))))
                  (if match-result (match:substring match-result 1)
                      (self-ref self-ref))))))
        (process-line process-line))
      "unknown"))

(use-modules
 (guix packages)
 (guix download)
 (guix git-download)
 (guix build-system python)
 (guix gexp)
 ((guix licenses) #:prefix license:)
 (gnu packages python-build)
 (gnu packages python-xyz)
 (gnu packages python-crypto)
 (gnu packages compression)
 (gnu packages python-compression)
 (gnu packages xdisorg)
 (gnu packages serialization)
 (gnu packages protobuf)
 (gnu packages python-web)
 (gnu packages check)
 (gnu packages sphinx)
 (gnu packages python-check)
 (gnu packages license)
 (gnu packages gnupg))

(define-public python-kaitaistruct
  (package
    (name "python-kaitaistruct")
    (version "0.10")
    (source
     (origin
       (method url-fetch)
       (uri (pypi-uri "kaitaistruct" version))
       (sha256
        (base32 "0ap5ka51gnc2mc4s1kqqsi6nb6zqv8wsrg17ryxazmkkj7idwi50"))))
    (build-system python-build-system)
    (home-page "https://kaitai.io")
    (native-inputs (list python-wheel))
    (synopsis
     "Declarative parser generator for binary data: runtime library for Python")
    (description
     "Kaitai Struct is a declarative language used for describing various binary
data structures, laid out in files or in memory - i.e. binary file formats,
network stream packet formats, etc.")
    (license license:expat)))

(define-public python-parver
  (package
    (name "python-parver")
    (version "0.3.1")
    (source
      (origin
        (method url-fetch)
        (uri (pypi-uri "parver" version))
        (sha256
          (base32 "1lyzqp8bz0n2kzabzl7k7g7cn90rlnrxjzva2p62gsfc7djy00n9"))))
    (build-system python-build-system)
    (arguments
     `(#:phases
       (modify-phases %standard-phases
         (add-after 'unpack 'relax-requirements
           (lambda _
             (substitute* "setup.py"
                          (("arpeggio[^']*") "arpeggio"))))
         (replace 'check
           (lambda* (#:key tests? #:allow-other-keys)
             (when tests?
               (invoke "pytest")))))))
    (propagated-inputs (list python-arpeggio python-attrs python-six))
    (native-inputs
      (list python-hypothesis
            python-pretend
            python-pytest))
    (home-page "https://github.com/RazerM/parver")
    (synopsis "Parse and manipulate version numbers")
    (description "Parver facilitates parsing and manipulation of
@url{https://www.python.org/dev/peps/pep-0440/,PEP 440} version numbers.")
    (license license:expat)))

(define-public python-pyopenssl-for-haketilo
  (let ((base python-pyopenssl))
    (package
      (inherit base)
      (version "22.0.0")
      (source
       (origin
         (inherit (package-source base))
         (uri (pypi-uri "pyOpenSSL" version))
         (sha256
          (base32
           "1gzihw09sqi71lwx97c69hab7w4rbnl6hhfrl6za3i5a4la1n2v6"))))
      (propagated-inputs
       (modify-inputs (package-propagated-inputs base)
         (replace "python-cryptography" python-cryptography-next))))))

(define-public python-urllib3-for-haketilo
  (let ((base python-urllib3))
    (package
      (inherit base)
      (propagated-inputs
       (modify-inputs (package-propagated-inputs base)
         (replace "python-cryptography" python-cryptography-next)
         (replace "python-pyopenssl" python-pyopenssl-for-haketilo))))))

(define-public python-requests-for-haketilo
  (let ((base python-requests))
    (package
      (inherit base)
      (propagated-inputs
       (modify-inputs (package-propagated-inputs base)
         (replace "python-urllib3" python-urllib3-for-haketilo))))))

(define-public python-werkzeug-for-haketilo
  (let ((base python-werkzeug))
    (package
      (inherit base)
      (propagated-inputs
       (modify-inputs (package-propagated-inputs base)
         (replace "python-requests" python-requests-for-haketilo))))))

(define-public python-flask-for-haketilo
  (let ((base python-flask))
    (package
      (inherit base)
      (propagated-inputs
       (modify-inputs (package-propagated-inputs base)
         (replace "python-werkzeug" python-werkzeug-for-haketilo))))))

(define-public mitmproxy
  (package
    (name "mitmproxy")
    (version "8.1.1")
    (source
     (origin
       (method git-fetch)
       (uri (git-reference
             (url "https://github.com/mitmproxy/mitmproxy")
             (commit (string-append "v" version))))
       (sha256
        (base32 "0kpzk8ci02vyjg9nqnpnadmgyaxxrpdydgfnm2xmxf1s4rzdcvwx"))
       (snippet
        '(begin
           ;; The player contains some minified JS. It would be possible to find
           ;; player sources elsewhere on the internet but there's no point in
           ;; doing do since we're not building the docs anyway.
           (delete-file "docs/src/assets/asciinema-player.js")
           #t))))
    (build-system python-build-system)
    (arguments
     `(#:phases
       (modify-phases %standard-phases
         (add-after 'unpack 'relax-requirements
           (lambda _
             (substitute* "setup.py"
               (("kaitaistruct>=0\\.7[^\"]*") "kaitaistruct")
               ;; The ">=2.8" req was there because older ldap3 lacked a crucial
               ;; ">=0.4.8" req for its dep, pyasn. It's not an issue for Guix
               ;; which ships with pyasn 4.8 anyway.
               (("ldap3>=2\\.8[^\"]*") "ldap3")
               (("protobuf>=3\\.14,<5") "protobuf")
               (("sortedcontainers>=2\\.3[^\"]*") "sortedcontainers")
               (("wsproto>=1\\.0[^\"]*") "wsproto")
               (("pytest-timeout[^\"]*<2[^\"]*") "pytest-timeout")
               (("pytest-asyncio[^\"]*<0.14[^\"]*") "pytest-asyncio"))
             (substitute* "test/mitmproxy/proxy/layers/http/test_http.py"
               (("isinstance\\(x, HTTPFlow\\)")
                "issubclass(type(x), HTTPFlow)"))))
         (replace 'check
           (lambda* (#:key tests? #:allow-other-keys)
             (when tests?
               (setenv "HOME" "/tmp")
               (invoke "pytest" "--timeout" "60")))))))
    (propagated-inputs
     (list python-asgiref
           python-blinker
           python-brotli
           python-cryptography-next
           python-flask-for-haketilo
           python-h11
           python-h2
           python-hyperframe
           python-kaitaistruct
           python-ldap3
           python-msgpack
           python-passlib
           python-protobuf
           python-pyopenssl-for-haketilo
           python-pyparsing
           python-pyperclip
           python-ruamel.yaml
           python-sortedcontainers
           python-tornado-6
           python-urwid
           python-wsproto
           python-publicsuffix2
           python-zstandard))
    (native-inputs
     (list python-parver
           python-pytest
           python-pytest-asyncio
           python-pytest-timeout))
    (home-page "https://mitmproxy.org/")
    (synopsis "A free interactive HTTPS proxy")
    (description
     "An interactive TLS-capable intercepting HTTP proxy for penetration testers
and software developers.  It can be used to intercept, inspect, modify and
replay web traffic such as HTTP/1, HTTP/2, WebSockets, or any other
SSL/TLS-protected protocols.")
    (license license:expat)))

(define-public python-immutables-for-haketilo
  (let ((base python-immutables))
    (package
      (inherit base)
      (version "0.19")
      (source
       (origin
         ;; Old version tarballs seem to be getting deleted from PyPI each time
         ;; a new version comes out.
         (method git-fetch)
         (uri (git-reference
               (url "https://github.com/MagicStack/immutables")
               (commit (string-append "v" version))))
         (sha256
          (base32
           "1awjylp4pl0jknwgnabg7kkj8f8883fkf99spsdrw1pj1acajvy9"))))
      (arguments
       `(#:phases
         (modify-phases %standard-phases
           (add-after 'unpack 'fix-expected-mypy-types
             (lambda _
               (substitute* "tests/test-data/check-immu.test"
                 (("builtins.str") "builtins.str*"))))
           (replace 'check
             (lambda* (#:key tests? #:allow-other-keys)
               (when tests?
                 (invoke "pytest")))))))
      (native-inputs
       (list python-pytest python-mypy)))))

(define-public python-types-requests
  (package
    (name "python-types-requests")
    (version "2.26.0")
    (source (origin
              (method url-fetch)
              (uri (pypi-uri "types-requests" version))
              (sha256
               (base32
                "10sq8jarr642vhw53k6zbf3hn2b8xfyrckwfngml4fj19g1whpnz"))))
    (build-system python-build-system)
    (home-page "https://github.com/python/typeshed")
    (synopsis "Typing stubs for requests")
    (description
     "This package provides a collection of library stubs for Python, with
static types.")
    (license license:asl2.0)))

;; Use this variant when building from a downloaded release tarball.
(define-public hydrilla
  (package
    (name "hydrilla")
    (version %hydrilla-version)
    (source (local-file %source-dir #:recursive? #t))
    (build-system python-build-system)
    (arguments
     `(#:phases
       (modify-phases %standard-phases
         (replace 'check
           (lambda* (#:key tests? #:allow-other-keys)
             (when tests?
               (invoke "pytest")))))))
    (propagated-inputs
     (list mitmproxy
           python-beautifulsoup4
           python-click
           python-flask-for-haketilo
           python-gnupg
           python-html5lib
           python-immutables-for-haketilo
           python-itsdangerous
           python-jsonschema
           reuse))
    (native-inputs
      (list python-setuptools-scm
            python-babel
            python-pytest
            python-pypa-build
            python-mypy
            python-types-requests))
    (home-page "https://hydrillabugs.koszko.org/projects/haketilo/wiki")
    (synopsis "Block JavaScript and add custom logic to web pages")
    (description "Haketilo HTTP proxy facilitates viewing of websites while
having their original JavaScript replaced by user-provided scripts. Haketilo
combines the functionalities of content blocker and user script manager. It can
be used with its script repository, Hydrilla.")
    (license (list license:agpl3+ license:gpl3+ license:cc0))))

;; Use this variant when building from a tarball generated under dist/. This
;; can be used to build from a git checkout after running `python3 -m build -s`
;; or similar.
(define-public hydrilla-dist-tarball
  (let ((base hydrilla)
        (filename (string-append "hydrilla-" %hydrilla-version ".tar.gz")))
    (package
      (inherit base)
      (source (local-file
               (string-append %source-dir "/dist/" filename))))))
