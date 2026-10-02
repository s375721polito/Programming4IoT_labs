import json

class catalog_manager:
    def __init__(self,file_name):
        self.catalog_file_name = file_name
        try:
            with open(self.catalog_file_name, 'r') as f:
                self.catalog = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Errore nel JSON: {e}")
            return
        except FileNotFoundError:
            print("File non trovato")
            return
        except Exception as e:
            print(f"Errore generico: {e}")
            return

    def search_by_name(self,name):
        if(not self.catalog["devicesList"]):
            return
        else:
            devices_list = self.catalog["devicesList"]
        for device in devices_list:
            if(device["deviceName"] == name):
                print(json.dumps(device))
                return

    def search_by_ID(self,ID):
        if(not self.catalog["devicesList"]):
            return
        else:
            devices_list = self.catalog["devicesList"]
        for device in devices_list:
            if(device["deviceID"] == ID):
                print(json.dumps(device))
                return
                

    def search_by_service(self,service):
        output_devices = []
        if(not self.catalog["devicesList"]):
            return
        else:
            devices_list = self.catalog["devicesList"]
        for device in devices_list:
            for serv in device["serviceDetails"]:
                if(serv["serviceType"] == service):
                    output_devices.append(device)
                    break
        print(json.dumps(output_devices))

    def search_by_measureType(self,measurement_type):
        output_devices = []
        if(not self.catalog["devicesList"]):
            return
        else:
            devices_list = self.catalog["devicesList"]
        for device in devices_list:
            if(measurement_type in device["measureType"]):
                output_devices.append(device)
        print(json.dumps(output_devices))

    def insert_device(self,new_device):
        if(not self.catalog["devicesList"]):
                    return
        else:
            devices_list = self.catalog["devicesList"]
        for i,device in enumerate(devices_list):
            if device["deviceID"] == new_device["deviceID"]:
                devices_list.pop(i)
                devices_list.append(new_device)
                return 
        devices_list.append(new_device)

    def print_all(self):
        print(json.dumps(self.catalog))

    def exit(self):
        try:
            with open(self.catalog_file_name, 'w') as f:
                json.dump(self.catalog,f)
        except json.JSONDecodeError as e:
            print(f"Errore nel JSON: {e}")
            return
        except FileNotFoundError:
            print("File non trovato")
            return
        except Exception as e:
            print(f"Errore generico: {e}")
            return

if __name__ == "main":
    manager = catalog_manager("catalog.json")
    manager.insert_device({})
    manager.exit()