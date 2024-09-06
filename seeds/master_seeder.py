from flask_seeder import Seeder
from sqlalchemy import MetaData

meta = MetaData()

class MasterSeeder(Seeder):

    def run(self):
        self.clear_data(self.db.session, self.db.metadata)
        from app.seeders.role_seeder import RoleSeeder
        RoleSeeder.run(self)
        
        from app.seeders.user_seeder import UserSeeder
        UserSeeder.run(self)
        
        from app.seeders.permission_seeder import PermissionSeeder
        PermissionSeeder.run(self)
        
    def clear_data(self, session, meta):
        for table in reversed(meta.sorted_tables):
            print (f'Clear table %s' % table)
            session.execute(table.delete())
        session.commit()