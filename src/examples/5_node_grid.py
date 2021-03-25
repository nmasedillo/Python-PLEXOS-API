from PlexosAPI import PlexosDatabase

# must have the full path or explicit relative path, otherwise it will complain about the folder not existing
file_name = r'.\my_5_node_grid.xml'

db = PlexosDatabase(file_name=file_name, force_new=True)

# region
db.add_region('R1')

# nodes
db.add_node('bus1', region='R1', V=10, Pload=0, Pmax=30, lat=1, lon=1, category='Nodes', is_slack=True)
db.add_node('bus2', region='R1', V=10, Pload=0, Pmax=999, lat=1, lon=1, category='Nodes')
db.add_node('bus3', region='R1', V=10, Pload=0, Pmax=999, lat=1, lon=1, category='Nodes')
db.add_node('bus4', region='R1', V=10, Pload=10, Pmax=999, lat=1, lon=1, category='Nodes')
db.add_node('bus5', region='R1', V=50, Pload=30, Pmax=999, lat=1, lon=1, category='Nodes', load_participation_factor=1)

# lines
db.add_line('bus1', 'bus2', name='L1_2', r=0.001, x=0.05, b=0.002, max_flow=100, min_flow=-100)

# transformers
db.add_transformer('bus4', 'bus5', 'TR1', 100, r=0.0001, x=0.05, b=0, category='Transformers')

# generators
db.add_generator('bus1', name='G1', units=1, max_capacity=50, fuel_price=10.5, heat_rate=10, category='Gas')
db.add_generator('bus3', name='G3', units=1, max_capacity=50, fuel_price=3.0, heat_rate=8, category='Fuel')

# battery
# db.add_battery('bus2', name='G2', units=1, capacity=20, max_power=10.5, initial_soc=0.8, charge_efficiency=0.99, category='Storage')

db.close()
