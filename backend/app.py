from flask import Flask
from flask_restful import Api

# Importing Auth Routes
from routes.auth_routes import (
    UserSignup,
    UserLogin,
    UserProfile,
    UserLogout,
    UserAuthStatus,
    UserPasswordResetRequest,
    UserPasswordReset,
    UserSendVerification,
    UserVerifyAccount,
    UserSettings
)

# Importing Character Routes
from routes.character_routes import (
    CharacterList,
    CharacterDetail,
    UserCharacters,
    SearchCharacters,
    CharacterLevelUp,
    CharactersBySystem,
    CharacterClone,
    CharacterArchive,
    CharacterExport,
    CharacterImport
)

# Importing RPG System Routes
from routes.rpgsystem_routes import (
    RPGSystemList,
    RPGSystemDetail,
    RPGSystemCreate,
    RPGSystemUpdate,
    RPGSystemDelete,
    RPGSystemSearch,
    RPGSystemPopular,
    RPGSystemDefaultSettings
)

# Importing Campaign Routes
from routes.campaign_routes import (
    CampaignList,
    CampaignDetail,
    CampaignCreate,
    CampaignUpdate,
    CampaignDelete,
    CampaignAddCharacter,
    CampaignRemoveCharacter,
    CampaignSessionLogs,
    CampaignAddSessionLog,
    CampaignHouseRules,
    CampaignSearch,
    CampaignNPCList,
    CampaignAddNPC,
    CampaignRemoveNPC,
    CampaignMonsterList,
    CampaignAddMonster,
    CampaignRemoveMonster
)

# Importing Monster Routes
from routes.monster_routes import (
    MonsterList,
    MonsterDetail,
    MonsterCreate,
    MonsterUpdate,
    MonsterDelete,
    HomebrewMonsterList,
    HomebrewMonsterCreate,
    HomebrewMonsterUpdate,
    HomebrewMonsterDelete,
    MonsterSearch,
    MonsterBookmark,
    ListBookmarkedMonsters
)

# Importing NPC Routes
from routes.npc_routes import (
    NPCList,
    NPCDetail,
    NPCCreate,
    NPCUpdate,
    NPCDelete,
    HomebrewNPCList,
    HomebrewNPCCreate,
    HomebrewNPCUpdate,
    HomebrewNPCDelete,
    NPCSearch,
    NPCBookmark,
    ListBookmarkedNPCs,
    NPCImport
)

# Importing Note Routes
from routes.note_routes import (
    NoteList,
    NoteDetail,
    NoteCreate,
    NoteUpdate,
    NoteDelete,
    NoteSearch,
    NoteShare
)

# Importing Utility Routes
from routes.utility_routes import (
    DashboardData,
    GlobalSearch
)

app = Flask(__name__)
api = Api(app)

# Registering Routes
# Auth Routes
api.add_resource(UserSignup, '/auth/register')
api.add_resource(UserLogin, '/auth/login')
api.add_resource(UserProfile, '/auth/profile/<int:user_id>')
api.add_resource(UserLogout, '/auth/logout')
api.add_resource(UserAuthStatus, '/auth/status')
api.add_resource(UserPasswordResetRequest, '/auth/password_reset_request')
api.add_resource(UserPasswordReset, '/auth/password_reset/<string:token>')
api.add_resource(UserSendVerification, '/auth/send_verification')
api.add_resource(UserVerifyAccount, '/auth/verify/<string:token>')
api.add_resource(UserSettings, '/auth/settings/<int:user_id>')

# Character Routes
api.add_resource(CharacterList, '/characters')
api.add_resource(CharacterDetail, '/characters/<int:character_id>')
api.add_resource(UserCharacters, '/users/<int:user_id>/characters')
api.add_resource(SearchCharacters, '/characters/search')
api.add_resource(CharacterLevelUp, '/characters/<int:character_id>/level_up')
api.add_resource(CharactersBySystem, '/characters/system/<int:rpg_system_id>')
api.add_resource(CharacterClone, '/characters/<int:character_id>/clone')
api.add_resource(CharacterArchive, '/characters/<int:character_id>/archive')
api.add_resource(CharacterExport, '/characters/<int:character_id>/export')
api.add_resource(CharacterImport, '/characters/import')

# RPG System Routes
api.add_resource(RPGSystemList, '/rpgsystems')
api.add_resource(RPGSystemDetail, '/rpgsystems/<int:rpg_system_id>')
api.add_resource(RPGSystemCreate, '/rpgsystems/new')
api.add_resource(RPGSystemUpdate, '/rpgsystems/<int:rpg_system_id>/update')
api.add_resource(RPGSystemDelete, '/rpgsystems/<int:rpg_system_id>/delete')
api.add_resource(RPGSystemSearch, '/rpgsystems/search')
api.add_resource(RPGSystemPopular, '/rpgsystems/popular')
api.add_resource(RPGSystemDefaultSettings, '/rpgsystems/<int:rpg_system_id>/default_settings')


# Campaign Routes
api.add_resource(CampaignList, '/campaigns')
api.add_resource(CampaignDetail, '/campaigns/<int:campaign_id>')
api.add_resource(CampaignCreate, '/campaigns/new')
api.add_resource(CampaignUpdate, '/campaigns/<int:campaign_id>/update')
api.add_resource(CampaignDelete, '/campaigns/<int:campaign_id>/delete')
api.add_resource(CampaignAddCharacter, '/campaigns/<int:campaign_id>/characters/add')
api.add_resource(CampaignRemoveCharacter, '/campaigns/<int:campaign_id>/characters/<int:character_id>/remove')
api.add_resource(CampaignSessionLogs, '/campaigns/<int:campaign_id>/logs')
api.add_resource(CampaignAddSessionLog, '/campaigns/<int:campaign_id>/logs/add')
api.add_resource(CampaignHouseRules, '/campaigns/<int:campaign_id>/house_rules')
api.add_resource(CampaignSearch, '/campaigns/search')
api.add_resource(CampaignNPCList, '/campaigns/<int:campaign_id>/npcs')
api.add_resource(CampaignAddNPC, '/campaigns/<int:campaign_id>/npcs/add')
api.add_resource(CampaignRemoveNPC, '/campaigns/<int:campaign_id>/npcs/<int:npc_id>/remove')
api.add_resource(CampaignMonsterList, '/campaigns/<int:campaign_id>/monsters')
api.add_resource(CampaignAddMonster, '/campaigns/<int:campaign_id>/monsters/add')
api.add_resource(CampaignRemoveMonster, '/campaigns/<int:campaign_id>/monsters/<int:monster_id>/remove')


# Monster Routes
api.add_resource(MonsterList, '/monsters')
api.add_resource(MonsterDetail, '/monsters/<int:monster_id>')
api.add_resource(MonsterCreate, '/monsters/new')
api.add_resource(MonsterUpdate, '/monsters/<int:monster_id>/update')
api.add_resource(MonsterDelete, '/monsters/<int:monster_id>/delete')
api.add_resource(MonsterSearch, '/monsters/search')
api.add_resource(HomebrewMonsterList, '/homebrew/monsters')
api.add_resource(HomebrewMonsterCreate, '/homebrew/monsters/new')
api.add_resource(HomebrewMonsterUpdate, '/homebrew/monsters/<int:homebrew_monster_id>/update')
api.add_resource(HomebrewMonsterDelete, '/homebrew/monsters/<int:homebrew_monster_id>/delete')
api.add_resource(MonsterBookmark, '/monsters/<int:monster_id>/bookmark')
api.add_resource(ListBookmarkedMonsters, '/monsters/bookmarks')


# NPC Routes
api.add_resource(NPCList, '/npcs')
api.add_resource(NPCDetail, '/npcs/<int:npc_id>')
api.add_resource(NPCCreate, '/npcs/new')
api.add_resource(NPCUpdate, '/npcs/<int:npc_id>/update')
api.add_resource(NPCDelete, '/npcs/<int:npc_id>/delete')
api.add_resource(NPCSearch, '/npcs/search')
api.add_resource(HomebrewNPCList, '/homebrew/npcs')
api.add_resource(HomebrewNPCCreate, '/homebrew/npcs/new')
api.add_resource(HomebrewNPCUpdate, '/homebrew/npcs/<int:homebrew_npc_id>/update')
api.add_resource(HomebrewNPCDelete, '/homebrew/npcs/<int:homebrew_npc_id>/delete')
api.add_resource(NPCBookmark, '/npcs/<int:npc_id>/bookmark')
api.add_resource(ListBookmarkedNPCs, '/npcs/bookmarks')
api.add_resource(NPCImport, '/npcs/import')

# Note Routes
api.add_resource(NoteList, '/notes')
api.add_resource(NoteDetail, '/notes/<int:note_id>')
api.add_resource(NoteCreate, '/notes/new')
api.add_resource(NoteUpdate, '/notes/<int:note_id>/update')
api.add_resource(NoteDelete, '/notes/<int:note_id>/delete')
api.add_resource(NoteSearch, '/notes/search')
api.add_resource(NoteShare, '/notes/<int:note_id>/share')

# Utility Routes
api.add_resource(DashboardData, '/dashboard/<int:user_id>/data')
api.add_resource(GlobalSearch, '/search')



if __name__ == '__main__':
    app.run(debug=True)
