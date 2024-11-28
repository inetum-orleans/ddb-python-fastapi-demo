local ddb = import 'ddb.docker.libjsonnet';

local domain = std.join('.', [std.extVar('core.domain.sub'), std.extVar('core.domain.ext')]);
local port_prefix = std.extVar('docker.port_prefix');
local app_workdir = '/app';

ddb.Compose() {
  services: {
    python: ddb.Build('python', context_use_project_home=true)
            + ddb.User()
            + ddb.Binary('python', app_workdir, 'python', '--label traefik.enable=false')
            + ddb.Binary('pip', app_workdir, 'pip', '--label traefik.enable=false')
            + ddb.Binary('poetry', app_workdir, 'poetry', '--label traefik.enable=false')
            + ddb.Binary('uvicorn', app_workdir, 'uvicorn')
            + ddb.VirtualHost('8000', domain, 'app')
            + {
              volumes: [
                ddb.path.project + ':' + app_workdir,
                'poetry-cache:/var/cache/pypoetry',
              ],
            },
  },
}
