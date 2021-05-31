### Installation

Only one requirement is to have docker runtime installed. Then, both versions of application can be launched by typing in:
```bash
$ docker compose up
```
in project main directory (either `vulnerable` or `well-secured`).

### Possible errors

If you try to launch the app after already having launched a different version previously and get this error:

*Error response from daemon: Conflict. The container name "/postgres-db" is already in use by container "6a6d3d17717bf43a6e016583f62c7300eeb38d84d00d1afe88a94b2a543721bc". You have to remove (or rename) that container to be able to reuse that name.*

Try running this command:
```bash
$ docker container rm $(docker container ls -aq)
```
