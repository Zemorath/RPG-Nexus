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

  // Log all the form fields' names
  const fields = form.getFields();
  fields.forEach((field) => {
    const type = field.constructor.name;
    const name = field.getName();
    console.log(`${name}`);
  });

  // Map the character data to the fillable fields on the PDF
  form.getTextField('CharacterName').setText(character.name);
  form.getTextField('ClassLevel').setText(character.class ? `${character.class.name} ${character.level}` : '');
  form.getTextField('ProfBonus').setText(String(character.proficiency_bonus || ''));
  form.getTextField('AC').setText(String(character.armor_class || ''));
  form.getTextField('HDTotal').setText(String(character.hit_dice_total || ''));
  form.getTextField('HD').setText(String(character.hit_dice || ''));

  // Ability scores and modifiers
  form.getTextField('STR').setText(String(character.ability_scores.Strength.override_score || character.ability_scores.Strength.total_score));
  form.getTextField('STRmod').setText(String(character.ability_scores.Strength.modifier));
  form.getTextField('DEX').setText(String(character.ability_scores.Dexterity.override_score || character.ability_scores.Dexterity.total_score));
  form.getTextField('DEXmod').setText(String(character.ability_scores.Dexterity.modifier));
  form.getTextField('CON').setText(String(character.ability_scores.Constitution.override_score || character.ability_scores.Constitution.total_score));
  form.getTextField('CONmod').setText(String(character.ability_scores.Constitution.modifier));
  form.getTextField('INT').setText(String(character.ability_scores.Intelligence.override_score || character.ability_scores.Intelligence.total_score));
  form.getTextField('INTmod').setText(String(character.ability_scores.Intelligence.modifier));
  form.getTextField('WIS').setText(String(character.ability_scores.Wisdom.override_score || character.ability_scores.Wisdom.total_score));
  form.getTextField('WISmod').setText(String(character.ability_scores.Wisdom.modifier));
  form.getTextField('CHA').setText(String(character.ability_scores.Charisma.override_score || character.ability_scores.Charisma.total_score));
  form.getTextField('CHamod').setText(String(character.ability_scores.Charisma.modifier));

  // Saving Throws
  const savingThrows = character.saving_throws || {};
  form.getTextField('ST Strength').setText(String(savingThrows.strength?.total || ''));
  form.getTextField('ST Dexterity').setText(String(savingThrows.dexterity?.total || ''));
  form.getTextField('ST Constitution').setText(String(savingThrows.constitution?.total || ''));
  form.getTextField('ST Intelligence').setText(String(savingThrows.intelligence?.total || ''));
  form.getTextField('ST Wisdom').setText(String(savingThrows.wisdom?.total || ''));
  form.getTextField('ST Charisma').setText(String(savingThrows.charisma?.total || ''));

  // Checkboxes for saving throws proficiency
  form.getCheckBox('Check STR').check(savingThrows.strength?.proficient || false);
  form.getCheckBox('Check DEX').check(savingThrows.dexterity?.proficient || false);
  form.getCheckBox('Check CON').check(savingThrows.constitution?.proficient || false);
  form.getCheckBox('Check INT').check(savingThrows.intelligence?.proficient || false);
  form.getCheckBox('Check WIS').check(savingThrows.wisdom?.proficient || false);
  form.getCheckBox('Check CHA').check(savingThrows.charisma?.proficient || false);

  // Skills
  const skills = character.skills || {};
  const skillsMapping = {
    Acrobatics: { field: 'Acrobatics', ability: 'Dexterity' },
    AnimalHandling: { field: 'Animal', ability: 'Wisdom' }, // Animal Handling
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
    SleightofHand: { field: 'SleightofHand', ability: 'Dexterity' }, // Sleight of Hand
    Stealth: { field: 'Stealth', ability: 'Dexterity' },
    Survival: { field: 'Survival', ability: 'Wisdom' }
  };
  const abilityScores = character.ability_scores;
  Object.keys(skillsMapping).forEach((skill) => {
    const skillData = skills[skill];
    const { field, ability } = skillsMapping[skill];
    if (skillData) {
      // Set the skill modifier field (e.g., Acrobatics, Animal)
      form.getTextField(field).setText(String(abilityScores[ability]?.modifier || ''));

      // Check the proficiency checkbox (e.g., Check Acrobatics, Check Animal)
      form.getCheckBox(`Check ${field}`).check(skillData.proficient || false);
    }
  });

  // Passive Wisdom (Perception)
  form.getTextField('Passive').setText(String(character.passive_perception || ''));

  // Proficiencies and Languages
  form.getTextField('ProficienciesLang').setText(character.proficiencies_and_languages || '');

  // Personality Traits
  form.getTextField('PersonalityTraits').setText(character.personality_traits || '');

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
