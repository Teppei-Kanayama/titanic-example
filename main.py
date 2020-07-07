import gokart
import luigi

import titanic

if __name__ == '__main__':
    luigi.configuration.LuigiConfigParser.add_config_path('./conf/environment.ini')
    gokart.run()
