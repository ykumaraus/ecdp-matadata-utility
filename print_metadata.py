#!/usr/bin/env python3
import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Print metadata inputs received from the workflow")
    parser.add_argument("--landing-zone", required=True, help="Landing zone name")
    parser.add_argument("--environment", required=True, help="Environment name")
    parser.add_argument("--service-domain", required=True, help="Service domain")
    args = parser.parse_args()

    print("Received metadata inputs:")
    print(f"Landing zone: {args.landing_zone}")
    print(f"Environment: {args.environment}")
    print(f"Service domain: {args.service_domain}")


if __name__ == "__main__":
    main()
