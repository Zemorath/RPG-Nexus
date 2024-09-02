import React, { useState } from 'react';
import { Link } from 'react-router-dom';

const Navbar = ({ onLogout }) => {
    console.log("Navbar received onLogout prop:", onLogout);
    const [showSystemsDropdown, setShowSystemsDropdown] = useState(false);
    const [showCampaignsDropdown, setShowCampaignsDropdown] = useState(false);
    const [showHomebrewDropdown, setShowHomebrewDropdown] = useState(false);
    const [showCharactersDropdown, setShowCharactersDropdown] = useState(false);
    const [showProfileDropdown, setShowProfileDropdown] = useState(false);

    return (
    <nav className="bg-primary p-4 shadow-md">
        <div className="container mx-auto flex justify-between items-center">
        <div className="flex space-x-6">
            {/* Systems Dropdown */}
            <div
            className="relative"
            onMouseEnter={() => setShowSystemsDropdown(true)}
            onMouseLeave={() => setShowSystemsDropdown(false)}
            >
            <button className="text-text font-bold hover:text-accent">Systems</button>
            {showSystemsDropdown && (
                <div className="absolute bg-secondary p-4 rounded-lg shadow-lg space-y-2">
                <Link to="/systems/view" className="block text-text hover:text-accent">View Systems</Link>
                <Link to="/systems/create" className="block text-text hover:text-accent">Create System</Link>
                </div>
            )}
            </div>

            {/* Campaigns Dropdown */}
            <div
            className="relative"
            onMouseEnter={() => setShowCampaignsDropdown(true)}
            onMouseLeave={() => setShowCampaignsDropdown(false)}
            >
            <button className="text-text font-bold hover:text-accent">Campaigns</button>
            {showCampaignsDropdown && (
                <div className="absolute bg-secondary p-4 rounded-lg shadow-lg space-y-2">
                <Link to="/campaigns/view" className="block text-text hover:text-accent">View Campaigns</Link>
                <Link to="/campaigns/create" className="block text-text hover:text-accent">Create Campaign</Link>
                </div>
            )}
            </div>

            {/* Homebrew Dropdown */}
            <div
            className="relative"
            onMouseEnter={() => setShowHomebrewDropdown(true)}
            onMouseLeave={() => setShowHomebrewDropdown(false)}
            >
            <button className="text-text font-bold hover:text-accent">Homebrew</button>
            {showHomebrewDropdown && (
                <div className="absolute bg-secondary p-4 rounded-lg shadow-lg space-y-2">
                <Link to="/homebrew/items" className="block text-text hover:text-accent">Homebrew Items</Link>
                <Link to="/homebrew/npcs" className="block text-text hover:text-accent">Homebrew NPCs</Link>
                <Link to="/homebrew/monsters" className="block text-text hover:text-accent">Homebrew Monsters</Link>
                </div>
            )}
            </div>

            {/* Characters Dropdown */}
            <div
            className="relative"
            onMouseEnter={() => setShowCharactersDropdown(true)}
            onMouseLeave={() => setShowCharactersDropdown(false)}
            >
            <button className="text-text font-bold hover:text-accent">Characters</button>
            {showCharactersDropdown && (
                <div className="absolute bg-secondary p-4 rounded-lg shadow-lg space-y-2">
                <Link to="/characters/view" className="block text-text hover:text-accent">View Characters</Link>
                <Link to="/characters/create" className="block text-text hover:text-accent">Create Character</Link>
                </div>
            )}
            </div>
        </div>

        {/* User Profile */}
        <div
            className="relative"
            onMouseEnter={() => setShowProfileDropdown(true)}
            onMouseLeave={() => setShowProfileDropdown(false)}
        >
            <button className="text-text font-bold hover:text-accent">Profile</button>
            {showProfileDropdown && (
            <div className="absolute bg-secondary p-4 rounded-lg shadow-lg space-y-2">
                <Link to="/settings" className="block text-text hover:text-accent">Settings</Link>
                <button
                onClick={() => {
                    console.log("Logout button clicked");
                    if (onLogout) {
                        onLogout();
                    } else {
                        console.error("onLogout function is not provided.");
                    }
                }}
                className="block text-text hover:text-accent w-full text-left"
                >
                Logout
                </button>
            </div>
            )}
        </div>
        </div>
    </nav>
    );
};

export default Navbar;
