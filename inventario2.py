#!/usr/bin/env python3
import json
import sys

def generate_inventory():
    # Estructura del inventario dinámico de Ansible
    inventory = {
        "all": {
            "children": ["ungrouped", "web", "bbdd", "lb"]
        },
        "ungrouped": {
            "hosts": []
        },
        "web": {
            "hosts": ["web1", "web2", "web3"],
            "vars": {
                "server_type": "frontend"
            }
        },
        "bbdd": {
            "hosts": ["bbdd1", "bbdd2"],
            "vars": {
                "server_type": "database"
            }
        },
        "lb": {
            "hosts": ["lb1"],
            "vars": {
                "server_type": "load_balancer"
            }
        },
        # _meta evita que Ansible tenga que llamar al script host por host para obtener sus variables
        "_meta": {
            "hostvars": {
                "web1": {"ansible_host": "192.168.1.11", "vcenter_cluster": "cluster-prod"},
                "web2": {"ansible_host": "192.168.1.12", "vcenter_cluster": "cluster-prod"},
                "web3": {"ansible_host": "192.168.1.13", "vcenter_cluster": "cluster-prod"},
                "bbdd1": {"ansible_host": "192.168.1.21", "vcenter_cluster": "cluster-db"},
                "bbdd2": {"ansible_host": "192.168.1.22", "vcenter_cluster": "cluster-db"},
                "lb1": {"ansible_host": "192.168.1.10", "vcenter_cluster": "cluster-prod"}
            }
        }
    }
    return inventory

if __name__ == "__main__":
    # Ansible llamará al script con el argumento --list
    if len(sys.argv) > 1 and sys.argv[1] == "--list":
        print(json.dumps(generate_inventory(), indent=2))
    else:
        # Formato básico por si se ejecuta vacío o para testing rápido
        print(json.dumps(generate_inventory(), indent=2))
