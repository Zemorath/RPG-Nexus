
import React, { Suspense, useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import spellConfig from '../components/config/spellConfig';

// Dynamically import the page component
const dynamicImport = (page) => React.lazy(() => import(`./${page}`));

const SelectSpellsPage = () => {
  const { systemId, characterId } = useParams();
  const [SpellPage, setSpellPage] = useState(null);

  useEffect(() => {
    const config = spellConfig[parseInt(systemId, 10)]; // Use parseInt to ensure systemId is an integer

    if (config) {
      const pageComponent = dynamicImport(config.spellPage);
      setSpellPage(pageComponent);
    } else {
      console.error('Unknown RPG system');
    }
  }, [systemId]);

  if (!SpellPage) {
    return <div>Loading...</div>;
  }

  return (
    <Suspense fallback={<div>Loading spell selection...</div>}>
      <SpellPage systemId={systemId} characterId={characterId} />
    </Suspense>
  );
};

export default SelectSpellsPage;


