import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate, useParams } from 'react-router-dom';

const EquipmentSelectionPage = () => {
  const { systemId, characterId } = useParams();
  const [items, setItems] = useState([]); // Full item list (original order)
  const [filteredItems, setFilteredItems] = useState([]); // Filtered item list
  const [inventory, setInventory] = useState([]); // Character's inventory
  const [searchTerm, setSearchTerm] = useState(''); // Search bar state
  const [selectedCategories, setSelectedCategories] = useState([]); // Categories toggled on
  const [uniqueSlotTypes, setUniqueSlotTypes] = useState([]); // Store unique slot types from the backend
  const [loading, setLoading] = useState(true);
  const [isInventoryOpen, setIsInventoryOpen] = useState(false); // Accordion state for inventory (collapsed by default)
  const [isItemsOpen, setIsItemsOpen] = useState(false); // Accordion state for available items (collapsed by default)
  const navigate = useNavigate();

  // Fetch items, character's existing inventory, and unique slot types from the backend
  useEffect(() => {
    const fetchData = async () => {
      try {
        const [itemsResponse, characterResponse, slotTypesResponse] = await Promise.all([
          axios.get(`http://127.0.0.1:5555/items/rpgsystem/${systemId}`),
          axios.get(`http://127.0.0.1:5555/api/characters/${characterId}`),
          axios.get(`http://127.0.0.1:5555/items/slot-types/rpgsystem/${systemId}`)
        ]);

        const allItems = itemsResponse.data;
        const characterInventory = characterResponse.data.inventory;

        setItems(allItems); // Store original items list
        setInventory(characterInventory); // Populate inventory with detailed items
        setFilteredItems(allItems); // Display all items, no need to filter

        setUniqueSlotTypes(slotTypesResponse.data); // Set the unique slot types for category filtering
        setLoading(false);
      } catch (error) {
        console.error('Error fetching data:', error);
        setLoading(false);
      }
    };

    fetchData();
  }, [systemId, characterId]);

  // Handle adding an item to inventory
  const handleAddToInventory = (item) => {
    setInventory((prevInventory) => [...prevInventory, item]);
  };

  // Handle removing an item from inventory
  const handleRemoveFromInventory = (item) => {
    setInventory((prevInventory) => prevInventory.filter((i) => i.id !== item.id));
  };

  // Handle search functionality
  const handleSearch = (event) => {
    const search = event.target.value.toLowerCase();
    setSearchTerm(search);
    setFilteredItems(
      items.filter(
        (item) =>
          item.name.toLowerCase().includes(search) ||
          item.description.toLowerCase().includes(search)
      )
    );
  };

  // Handle toggling categories
  const handleCategoryToggle = (category) => {
    const updatedCategories = selectedCategories.includes(category)
      ? selectedCategories.filter((cat) => cat !== category)
      : [...selectedCategories, category];

    setSelectedCategories(updatedCategories);

    if (updatedCategories.length > 0) {
      setFilteredItems(items.filter((item) => updatedCategories.includes(item.slot_type)));
    } else {
      setFilteredItems(items);
    }
  };

  // Submit selected items to backend
  const handleSubmit = async () => {
    try {
      await axios.post(`http://127.0.0.1:5555/api/characters/update-items`, {
        character_id: characterId,
        item_ids: inventory.map((item) => item.id),
      });
      navigate(`/character/summary/${systemId}/${characterId}`);
    } catch (error) {
      console.error('Error submitting inventory:', error);
    }
  };

  if (loading) {
    return <div>Loading items...</div>;
  }

  return (
    <div className="min-h-screen bg-background text-text p-8">
      <div className="container mx-auto">
        <div className="flex justify-between mb-8">
          {/* Back Button */}
          <button
            onClick={() => navigate(`/character/create/background/${systemId}/${characterId}`)}
            className="bg-accent text-background py-2 px-4 rounded hover:bg-text hover:text-background transition duration-300"
          >
            ← Back
          </button>

          {/* Submit Button */}
          <button
            onClick={handleSubmit}
            className="bg-accent text-background py-2 px-6 rounded hover:bg-text hover:text-background transition duration-300"
          >
            Submit
          </button>
        </div>

        {/* Search Bar */}
        <div className="mb-8 text-center">
          <input
            type="text"
            placeholder="Search items..."
            value={searchTerm}
            onChange={handleSearch}
            className="p-2 rounded bg-secondary text-text w-full max-w-md"
          />
        </div>

        {/* Category Toggle Buttons */}
        <div className="mb-8 grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-4 justify-center">
          {uniqueSlotTypes.map((category) => (
            <button
              key={category}
              className={`py-2 px-4 rounded text-center ${selectedCategories.includes(category) ? 'bg-accent text-background' : 'bg-secondary text-text'}`}
              onClick={() => handleCategoryToggle(category)}
            >
              {category}
            </button>
          ))}
        </div>

        {/* Accordion for Inventory */}
        <div className="mb-8 text-center">
          <button
            className="w-full bg-secondary p-4 rounded-lg shadow-lg text-center max-w-lg mx-auto"
            onClick={() => setIsInventoryOpen(!isInventoryOpen)}
          >
            <h2 className="text-xl font-bold">Inventory {isInventoryOpen ? '↑' : '↓'}</h2>
          </button>
          {isInventoryOpen && (
            <div className="bg-secondary p-4 rounded-lg shadow-lg overflow-y-scroll h-64 text-center max-w-lg mx-auto">
              {inventory.length > 0 ? (
                inventory.map((item) => (
                  <div key={item.id} className="flex justify-between items-center mb-4 border border-accent rounded p-4 shadow">
                    <div>
                      <h3 className="text-lg font-bold">{item.name}</h3>
                      <p>Rarity: {item.rarity}</p>
                      <p>Weight: {item.weight} lbs</p>
                      <p>Cost: {item.cost} gold</p>
                    </div>
                    <button
                      onClick={() => handleRemoveFromInventory(item)}
                      className="bg-red-600 text-background py-2 px-4 rounded hover:bg-text hover:text-background transition duration-300"
                    >
                      Remove
                    </button>
                  </div>
                ))
              ) : (
                <p className="text-center">No items in inventory</p>
              )}
            </div>
          )}
        </div>

        {/* Accordion for Available Items */}
        <div className="mb-8 text-center">
          <button
            className="w-full bg-secondary p-4 rounded-lg shadow-lg text-center max-w-lg mx-auto"
            onClick={() => setIsItemsOpen(!isItemsOpen)}
          >
            <h2 className="text-xl font-bold">Available Items {isItemsOpen ? '↑' : '↓'}</h2>
          </button>
          {isItemsOpen && (
            <div className="bg-secondary p-4 rounded-lg shadow-lg overflow-y-scroll h-96 text-center max-w-lg mx-auto">
              {filteredItems.length > 0 ? (
                filteredItems.map((item) => (
                  <div key={item.id} className="flex justify-between items-center mb-4 border border-accent rounded p-4 shadow">
                    <div>
                      <h3 className="text-lg font-bold">{item.name}</h3>
                      <p>Rarity: {item.rarity}</p>
                      <p>Weight: {item.weight} lbs</p>
                      <p>Cost: {item.cost} gold</p>
                    </div>
                    <button
                      onClick={() => handleAddToInventory(item)}
                      className="bg-accent text-background py-2 px-4 rounded hover:bg-text hover:text-background transition duration-300"
                    >
                      Add
                    </button>
                  </div>
                ))
              ) : (
                <p className="text-center">No items found</p>
              )}
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default EquipmentSelectionPage;
