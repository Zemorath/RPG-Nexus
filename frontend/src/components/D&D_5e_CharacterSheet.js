import { PDFDocument } from 'pdf-lib';
import { saveAs } from 'file-saver';
import axios from 'axios';

const generateCharacterSheet = async (characterId) => {
  // Fetch the calculated character data using the CharacterCalculation route
  const calculatedCharacterResponse = await axios.get(`http://127.0.0.1:5555/api/characters/calculate/${characterId}`);
  const character = calculatedCharacterResponse.data;

  // Load the fillable D&D 5e character sheet PDF
  const url = '/pdfs/D&D_5e.pdf';
  const existingPdfBytes = await fetch(url).then((res) => res.arrayBuffer());

  // Load the PDF with pdf-lib
  const pdfDoc = await PDFDocument.load(existingPdfBytes);

  // Get the form and the fields
  const form = pdfDoc.getForm();
  

  // Map character data to the fillable fields on the PDF
  form.getTextField('CharacterName').setText(character.name);
  form.getTextField('ClassLevel').setText(character.class ? `${character.class.name} ${character.level}` : '');
  form.getTextField('ProfBonus').setText(String(character.proficiency_bonus || ''));
  form.getTextField('AC').setText(String(character.armor_class || ''));
  form.getTextField('HDTotal').setText(String(character.hit_dice_total || ''));
  form.getTextField('HD').setText(String(character.hit_dice || ''));

  // Ability scores and modifiers
  const abilityScores = character.ability_scores;
  Object.entries(abilityScores).forEach(([ability, score]) => {
    const modifier = Math.floor((score - 10) / 2);
    form.getTextField(ability.substring(0, 3).toUpperCase()).setText(String(score));
    form.getTextField(`${ability.substring(0, 3).toUpperCase()}mod`).setText(String(modifier));
  });

  // Saving Throws
  const savingThrows = character.saving_throws || {};
  const abilities = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma'];

  abilities.forEach((ability) => {
    const savingThrowData = savingThrows[ability];
    if (savingThrowData) {
      const abilityModifier = Math.floor((abilityScores[ability] - 10) / 2);
      const totalBonus = abilityModifier + (savingThrowData.proficient ? character.proficiency_bonus : 0);
      
      // Set the saving throw total
      form.getTextField(`ST ${ability}`).setText(String(totalBonus));
      
      // Set the proficiency checkbox
      const checkboxField = form.getCheckBox(`Check ${ability.substring(0, 3).toUpperCase()}`);
      if (savingThrowData.proficient) {
        checkboxField.check();
      } else {
        checkboxField.uncheck();
      }
    } else {
      // If there's no saving throw data, just set the ability modifier
      const abilityModifier = Math.floor((abilityScores[ability] - 10) / 2);
      form.getTextField(`ST ${ability}`).setText(String(abilityModifier));
      form.getCheckBox(`Check ${ability.substring(0, 3).toUpperCase()}`).uncheck();
    }
  });

  // Skills
  const skills = character.skills || {};
  const skillsMapping = {
    Acrobatics: { field: 'Acrobatics', ability: 'Dexterity' },
    AnimalHandling: { field: 'Animal', ability: 'Wisdom' },
    Arcana: { field: 'Arcana', ability: 'Intelligence' },
    Athletics: { field: 'Athletics', ability: 'Strength' },
    Deception: { field: 'Deception', ability: 'Charisma' },
    History: { field: 'History', ability: 'Intelligence' },
    Insight: { field: 'Insight', ability: 'Wisdom' },
    Intimidation: { field: 'Intimidation', ability: 'Charisma' },
    Investigation: { field: 'Investigation', ability: 'Intelligence' },
    Medicine: { field: 'Medicine', ability: 'Wisdom' },
    Nature: { field: 'Nature', ability: 'Intelligence' },
    Perception: { field: 'Perception', ability: 'Wisdom' },
    Performance: { field: 'Performance', ability: 'Charisma' },
    Persuasion: { field: 'Persuasion', ability: 'Charisma' },
    Religion: { field: 'Religion', ability: 'Intelligence' },
    SleightofHand: { field: 'SleightofHand', ability: 'Dexterity' },
    Stealth: { field: 'Stealth', ability: 'Dexterity' },
    Survival: { field: 'Survival', ability: 'Wisdom' }
  };

  Object.entries(skillsMapping).forEach(([skill, { field, ability }]) => {
    const skillData = skills[skill];
    if (skillData) {
      const abilityModifier = Math.floor((abilityScores[ability] - 10) / 2);
      const totalBonus = abilityModifier + (skillData.proficient ? character.proficiency_bonus : 0) + (skillData.bonus || 0);
      form.getTextField(field).setText(String(totalBonus));
      
      // Only check the box if the skill is proficient
      if (skillData.proficient) {
        form.getCheckBox(`Check ${field}`).check();
      } else {
        form.getCheckBox(`Check ${field}`).uncheck();
      }
    }
  });

  // Passive Wisdom (Perception)
  const passiveWisdom = 10 + Math.floor((abilityScores['Wisdom'] - 10) / 2);
  form.getTextField('Passive').setText(String(passiveWisdom));

  // Physical features and character traits
  const physicalFeatures = character.physical_features || {};
  form.getTextField('Age').setText(physicalFeatures.age || '');
  form.getTextField('Height').setText(physicalFeatures.height || '');
  form.getTextField('Weight').setText(physicalFeatures.weight || '');
  form.getTextField('Eyes').setText(physicalFeatures.eyes || '');
  form.getTextField('Skin').setText(physicalFeatures.skin || '');
  form.getTextField('Hair').setText(physicalFeatures.hair || '');

  form.getTextField('PersonalityTraits').setText(physicalFeatures.traits?.join(', ') || '');
  form.getTextField('Ideals').setText(physicalFeatures.ideals?.join(', ') || '');
  form.getTextField('Bonds').setText(physicalFeatures.bonds?.join(', ') || '');
  form.getTextField('Flaws').setText(physicalFeatures.flaws?.join(', ') || '');
  form.getTextField('Allies').setText(physicalFeatures.allies?.join(', ') || '');
  form.getTextField('FactionName').setText(physicalFeatures.organizations?.join(', ') || '');

  // Equipment (Inventory)
  const inventoryResponse = await axios.get(`http://127.0.0.1:5555/api/characters/${characterId}/inventory`);
  const inventory = inventoryResponse.data;
  const inventoryText = inventory.map(item => `${item.name} (${item.quantity})`).join(', ');
  form.getTextField('Equipment').setText(inventoryText);

  // Other fields 
  form.getTextField('Background').setText(character.background.name);
  form.getTextField('Alignment').setText(character.alignment.name);
  form.getTextField('Race').setText(character.race.name);
  form.getTextField('Initiative').setText(String(character.initiative));
  form.getTextField('HPMax').setText(String(character.health));
  form.getTextField('HPCurrent').setText(String(character.health));

  // Weapons (if available)
  if (character.weapons?.length > 0) {
    form.getTextField('Wpn Name').setText(character.weapons[0].name);
    form.getTextField('Wpn1 AtkBonus').setText(String(character.weapons[0].attack_bonus || ''));
    form.getTextField('Wpn1 Damage').setText(character.weapons[0].damage || '');
  }

  // Save the modified PDF and download it
  const pdfBytes = await pdfDoc.save();
  const blob = new Blob([pdfBytes], { type: 'application/pdf' });
  saveAs(blob, `${character.name}_CharacterSheet.pdf`);
};

export default generateCharacterSheet;