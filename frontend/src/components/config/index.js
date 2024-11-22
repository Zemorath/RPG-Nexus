import { EdgeOfTheEmpireConfig } from "./edge_of_the_empire";
import { DnD5eConfig } from "./dnd_5e";
import { PathfinderConfig } from "./pathfinder";
import { CallOfCthulhuConfig } from "./call_of_cthulhu";
import { ShadowrunConfig } from "./shadowrun";
import { MothershipConfig } from "./mothership";

const RPGConfigs = {
  1: DnD5eConfig,                 // Dungeons & Dragons 5th Edition
  2: PathfinderConfig,            // Pathfinder
  3: CallOfCthulhuConfig,         // Call of Cthulhu
  4: ShadowrunConfig,             // Shadowrun
  5: EdgeOfTheEmpireConfig,       // Star Wars: Edge of the Empire
  6: MothershipConfig,            // Mothership RPG
};

export default RPGConfigs;
