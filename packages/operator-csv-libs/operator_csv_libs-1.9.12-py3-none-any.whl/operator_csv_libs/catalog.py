import os
import sys
import logging
import json
from natsort import natsorted

# Setup logging to stdout
log = logging.getLogger(__name__)
out_hdlr = logging.StreamHandler(sys.stdout)
out_hdlr.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s', '%Y-%m-%d %H:%M:%S'))
out_hdlr.setLevel(logging.INFO)
log.addHandler(out_hdlr)
log.setLevel(logging.INFO)

'''
Base Class for Catalog Exceptions
'''
class CatalogError(Exception):
    pass


'''
Class for interacting with File based Catalog files
'''
class Catalog:

    def __init__(self, file, indent=4):
        self.channels = []
        self.package = ''
        self.bundles = []
        self.indent = indent

        if not os.path.exists(file):
            raise CatalogError(f"Cannot find catalog.json file {file}")

        # Read in data from single catalog file
        if os.path.isfile(file):
            with open(file) as stream:
                separators = []
                lines = stream.readlines()
                count = 0
                startValue = 0
                for line in lines:
                    if line == '}\n' or line == '}':
                        separators.append(count)
                    count += 1
                for s in separators:
                    data = json.loads(''.join(lines[startValue:s+1]))
                    if 'schema' not in data:
                        raise CatalogError(f"Cannot find a schema value in {data}")

                    if data['schema'] == 'olm.package':
                        if self.package != '':
                            raise CatalogError(f"Found 2 packages in a single file, unexpected use case. Please update the code base")
                        self.package = data
                    elif data['schema'] == 'olm.channel':
                        self.channels.append(data)
                    elif data['schema'] == 'olm.bundle':
                        self.bundles.append(data)

                    startValue = s+1
        # Read in data from a directory of json files
        elif os.path.isdir(file):
            for f in os.listdir(file):
                with open(f"{file}/{f}") as stream:
                    data = json.load(stream)
                    if 'schema' not in data:
                        raise CatalogError(f"Cannot find a schema value in {data}")

                    if data['schema'] == 'olm.package':
                        if self.package != '':
                            raise CatalogError(f"Found 2 packages in a single file, unexpected use case. Please update the code base")
                        self.package = data
                    elif data['schema'] == 'olm.channel':
                        self.channels.append(data)
                    elif data['schema'] == 'olm.bundle':
                        self.bundles.append(data)

    def get_channels(self):
        return self.channels

    def get_bundles(self):
        return self.bundles

    def get_default_channel(self):
        return self.package['defaultChannel']

    def set_default_channel(self, channel):
        self.package['defaultChannel'] = channel

    def write_new_file(self, filename='./catalog.json'):
        with open(filename, 'w') as f:
            json.dump(self.package, f, indent=self.indent)
            f.write("\n")
            for c in self.channels:
                json.dump(c, f, indent=self.indent)
                f.write("\n")
            for b in self.bundles:
                json.dump(b, f, indent=self.indent)
                f.write("\n")
    
    def write_new_dir(self, directory='.'):
        with open(f"{directory}/olm.package-{self.package['name']}.json", 'w') as package_file:
            json.dump(self.package, package_file, indent=self.indent)
        for c in self.channels:
            with open(f"{directory}/olm.channel-{c['name']}.json", 'w') as channel_file:
                json.dump(c, channel_file, indent=self.indent)
        for b in self.bundles:
            with open(f"{directory}/olm.bundle-{b['name']}.json", 'w') as bundle_file:
                json.dump(b, bundle_file, indent=self.indent)

    def remove_channel(self, channel):
        for c in self.channels:
            if c['name'] == channel:
                for e in c['entries']:
                    self.remove_bundle(e['name'])
                self.channels.remove(c)

    def remove_bundle(self, name):
        for b in self.bundles:
            if b['name'] == name:
                self.bundles.remove(b)

    def add_channel(self, channel, package):
        self.channels.append({
            "schema": "olm.channel",
            "name": channel,
            "package": package, 
            "entries": []
        })
    
    def add_channel_entry(self, channel, name, skiprange=None, replaces=None):
        data = {}
        data['name'] = name
        if skiprange:
            data['skiprange'] = skiprange
        if replaces:
            data['replaces'] = replaces
        for c in self.channels:
            if c['name'] == channel:
                if 'entries' in c:
                    c['entries'] = []
                c['entries'].append(data)
                
    def get_latest_channel_entry(self, channel):
        names = [e['name'] for e in channel['entries'] ]
        names = natsorted(names)
        return names[-1]
    
    def __str__(self):
        ret = ''
        ret += f"Package: {self.package['name']}\n"
        for c in self.channels:
            ret += f"\tChannel: {c['name']}\tLatest entry: {self.get_latest_channel_entry(c)}\n"
        return ret

