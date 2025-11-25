# Ubuntu Transition Tracker Operator


**Ubuntu  Transition Tracker Operator** is a [charm](https://juju.is/charms-architecture) for deploying an Ubuntu transition tracker environment.

This reposistory contains the code for the charm, the application is coming from the `ben` package and the [configs repository](https://git.launchpad.net/~ubuntu-transition-trackers/ubuntu-transition-tracker/+git/configs).

## Basic usage

Assuming you have access to a bootstrapped [Juju](https://juju.is) controller, you can deploy the charm with:

```bash
❯ juju deploy ubuntu-transition-tracker
```

Once the charm is deployed, you can check the status with Juju status:

```bash
❯ $ juju status
Model        Controller  Cloud/Region         Version  SLA          Timestamp
welcome-lxd  lxd         localhost/localhost  3.6.7    unsupported  13:29:50+02:00

App       Version  Status  Scale  Charm             Channel  Rev  Exposed  Message
transition-tracker           active      1  ubuntu-transition-tracker             0  no

Unit          Workload  Agent  Machine  Public address  Ports  Message
transition-tracker/0*  active    idle    1       10.142.46.109

Machine  State    Address        Inst id         Base          AZ  Message
1        started  10.142.46.109  juju-fd4fe1-1   ubuntu@24.04      Running
```

On first start up, the charm will install the application and install a systemd timer unit to trigger tracker updates on a regular basis.

To refresh the report, you can use the provided Juju [Action](https://documentation.ubuntu.com/juju/3.6/howto/manage-actions/):

```bash
❯ juju run ubuntu-transition-tracker/0 refresh"
```

## Contribute to Ubuntu Transition Tracker Operator

Ubuntu Transition Tracker Operator is open source and part of the Canonical family. We would love your help.

If you're interested, start with the [contribution guide](CONTRIBUTING.md).

## License and copyright

Ubuntu Transition Tracker Operator is released under the [GPL-3.0 license](LICENSE).
