# Decision sources and evidence limits

Checked November 4, 2026. Official sources support available mechanisms/version lines; project policies and numerical limits are explicit design choices, not claims that a standard mandates them.

| Subject | Primary reference | Use |
| --- | --- | --- |
| Laravel/PHP compatibility | [Laravel 13 Release Notes](https://laravel.com/framework/docs/13.x/releases) | Framework/runtime line |
| PHP maintenance | [PHP supported versions](https://www.php.net/supported-versions.php) | Maintain PHP 8.4 security patches |
| Database | [MySQL 8.4 manual](https://dev.mysql.com/doc/refman/8.4/en/) | InnoDB/LTS line |
| Build runtime | [Node.js releases](https://nodejs.org/en/about/previous-releases) | Node 24 LTS build runtime |
| Authentication | [Fortify](https://laravel.com/framework/docs/13.x/fortify) | Authentication backend; project disables registration |
| OAuth2 | [Passport](https://laravel.com/framework/docs/13.x/passport), [League client](https://oauth2-client.thephpleague.com/usage/) | Authorization code, state, PKCE |
| Delegated API signing | [Lcobucci JWT](https://github.com/lcobucci/jwt) | JWT library; project pins validation policy |
| Native Git transport | [git-http-backend](https://git-scm.com/docs/git-http-backend) | CGI Smart HTTP and export/auth controls |
| Admission proxy | [Nginx auth_request](https://nginx.org/en/docs/http/ngx_http_auth_request_module.html) | Authorization subrequests; verify build module |
| PDF | [Dompdf](https://github.com/dompdf/dompdf) | Trusted-template local rendering |
| Backup | [restic repository setup](https://restic.readthedocs.io/en/stable/030_preparing_a_new_repo.html) | Encrypted independent backup repository |
| Accessibility | [WCAG 2.2](https://www.w3.org/TR/WCAG22/) | AA target; no certification claim |
| Software versions | [Semantic Versioning](https://semver.org/) | Software public-contract version policy, independent of MVP scope |

The sibling Git hosting reference is not adopted or copied. Its source rights and actual deployed security behavior have not been validated. No external credentials, licensing permission, independent Advisor review, runtime installation or live recovery evidence is inferred from documentation research.
