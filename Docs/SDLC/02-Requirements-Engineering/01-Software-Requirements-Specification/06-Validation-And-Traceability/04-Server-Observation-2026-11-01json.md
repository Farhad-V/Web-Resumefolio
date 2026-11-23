
<a id="validation-and-traceability-server-observation-2026-11-01"></a>

# server-observation-2026-11-01.json

Dated supporting evidence. Consult the [evidence guide](README.md) for context; use the [traceability matrix](../../03-Requirements-Traceability-Matrix/README.md) for current criterion lookup. The record below retains its original observations and limits.

<details>
<summary>Open the full recorded evidence</summary>

```json
{
  "activity": "RV-D04 / LOG-002",
  "recorded_date": "2026-11-01",
  "provenance": "Owner-supplied Hetzner screenshots and SSH output in this conversation; no fresh server connection by this documentation update",
  "observed_login_banner_time_utc": "2026-11-01 08:37:57",
  "allocation": {
    "provider": "Hetzner",
    "plan_as_shown": "CX23",
    "location_as_shown": "Falkenstein",
    "vcpu": 2,
    "ram_GB": 4,
    "local_disk_GB": 40
  },
  "guest": {
    "os_banner": "Ubuntu 24.04.4 LTS",
    "kernel_banner": "6.8.0-124-generic",
    "architecture": "x86_64"
  },
  "free_h_as_shown": {
    "total": "3.7Gi",
    "used": "924Mi",
    "free": "404Mi",
    "shared": "29Mi",
    "buff_cache": "2.7Gi",
    "available": "2.8Gi",
    "swap_total": "0B"
  },
  "df_h_root_as_shown": {
    "size": "38G",
    "used": "6.5G",
    "available": "30G",
    "use_percent": "19%"
  },
  "observed_running_services": [
    "nginx",
    "mysql",
    "php8.3-fpm"
  ],
  "observed_nginx_configuration": {
    "server_names": [
      "resumefolio.de",
      "www.resumefolio.de"
    ],
    "root": "/var/www/web-resume-management-system/public",
    "artisan_found": "/var/www/web-resume-management-system/artisan"
  },
  "limits": [
    "Low-load point-in-time observation, not combined-workload capacity",
    "No exact Laravel/MySQL/dependency version determined",
    "No independent backup destination or restoration verified",
    "No live DNS/TLS/renewal or provider access finding",
    "No numerical quality/recovery target or product-policy decision",
    "No credentials, key contents, fingerprint comments or personal login IPs recorded"
  ],
  "tracking": [
    "DEP-01",
    "ASM-01",
    "Q-D24",
    "Q-D25",
    "Q-D26",
    "Q-D27"
  ]
}
```

</details>
