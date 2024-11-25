local ddb = import 'ddb.docker.libjsonnet';

local domain = std.join('.', [std.extVar("core.domain.sub"), std.extVar("core.domain.ext")]);
local port_prefix = std.extVar("docker.port_prefix");

local web_workdir = "/var/www/html";
local app_workdir = "/app";

local prefix_port(port, output_port = null)= [port_prefix + (if output_port == null then std.substr(port, std.length(port) - 2, 2) else output_port) + ":" + port];

ddb.Compose() {
	"services": {
		"python": ddb.Build("python", context_use_project_home=true)
		    + ddb.User()
		    + ddb.Binary("python", web_workdir, "python")
		    + ddb.Binary("pip", web_workdir, "pip")
		    + ddb.Binary("poetry", web_workdir, "poetry")
			+ ddb.Binary("uvicorn", web_workdir, "uvicorn")
			+ ddb.VirtualHost("8000", domain, "app")
		    + {
                volumes: [
                    ddb.path.project + ":" + web_workdir,
					"poetry-cache:/var/cache/pypoetry"
                ]
            }
	}
}

