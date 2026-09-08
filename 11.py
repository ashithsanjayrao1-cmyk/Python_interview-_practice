import copy

server_configs = [["server1","active"],["server2","inactive"]]

backup_configs = server_configs.copy()
backup_configs[0][1] = "inactive"

print(server_configs[0][1])
print(backup_configs[0][1])

