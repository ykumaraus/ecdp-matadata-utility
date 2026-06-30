#!/usr/bin/env bash
set -euo pipefail

landing_zone="${1:-}"
environment="${2:-}"
service_domain="${3:-}"

if [[ -z "$landing_zone" || -z "$environment" || -z "$service_domain" ]]; then
  echo "Usage: $0 <landing_zone> <environment> <service_domain>" >&2
  exit 1
fi

python3 ./print_metadata.py \
  --landing-zone "$landing_zone" \
  --environment "$environment" \
  --service-domain "$service_domain"
