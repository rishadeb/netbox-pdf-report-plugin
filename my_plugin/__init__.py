from extras.plugins import PluginConfig

class MyPluginConfig(PluginConfig):
    name = 'my_plugin'
    verbose_name = 'My Plugin'
    description = 'A plugin to export IP addresses to PDF'
    version = '1.2.0'

config = MyPluginConfig