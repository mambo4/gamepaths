# Id Project Classes

Classes for local workspace independent file routing

## What is an asset path

<root><project> <"source" or "game"> <dept> [<dept dir tree>...] <asset name> [<component tree>...] <asset_name_assettype>.<ext>

ROOT: <root><project> <"source" or "game">
ASSET_PATH: <dept> [<dept dir tree>...] <asset name> 
COMPONENT_PATH: [<component tree>...] 
FILENAME:  <asset_name_assettype>.<ext>

## IdProjectClient
Holds info about user, perforce port, source and game project workspaces
read/writes data to json

#### properties
- IdProjectClient.user
- IdProjectClient.server
- IdProjectClient.project_name
- IdProjectClient.source_client
- IdProjectClient.source_root
- IdProjectClient.game_client
- IdProjectClient.game_root

#### methods

- load_project_client(project_name) - reads the json file, loads data for project_name
- select_project_client() - reads the json file, prompts user to select for  list of project names
- create_project_client()
- edit_project_client()
- write_project_client_data()

#### json data
    {
    	"projectA": {
    		"project_name": "projectA",
    		"user": "mambo4",
    		"server": "sever.company.com:1234",
    		"source_client": "mambo4_projectA_source",
    		"source_root": "C:/projectA/source",
    		"game_client": "mambo4_projectA_game",
    		"game_root": "C:/projectA"
    	},

    	"projectB": {...}

    }

## IdProjectPath

#### properties

#### methods

#### json data

## IdAssetPath

#### properties

#### methods

#### json data