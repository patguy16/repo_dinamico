{
  "all": {
    "children": [
      "ungrouped",
      "web",
      "bbdd",
      "lb"
    ]
  },
  "ungrouped": {
    "hosts": []
  },
  "web": {
    "hosts": [
      "web1",
      "web2",
      "web3"
    ],
    "vars": {
      "server_type": "frontend"
    }
  },
  "bbdd": {
    "hosts": [
      "bbdd1",
      "bbdd2"
    ],
    "vars": {
      "server_type": "database"
    }
  },
  "lb": {
    "hosts": [
      "lb1"
    ],
    "vars": {
      "server_type": "load_balancer"
    }
  },
  "_meta": {
    "hostvars": {
      "web1": {
        "ansible_host": "192.168.1.11",
        "vcenter_cluster": "cluster-prod"
      },
      "web2": {
        "ansible_host": "192.168.1.12",
        "vcenter_cluster": "cluster-prod"
      },
      "web3": {
        "ansible_host": "192.168.1.13",
        "vcenter_cluster": "cluster-prod"
      },
      "bbdd1": {
        "ansible_host": "192.168.1.21",
        "vcenter_cluster": "cluster-db"
      },
      "bbdd2": {
        "ansible_host": "192.168.1.22",
        "vcenter_cluster": "cluster-db"
      },
      "lb1": {
        "ansible_host": "192.168.1.10",
        "vcenter_cluster": "cluster-prod"
      }
    }
  }
}
