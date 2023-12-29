import React, { useState } from 'react';

const Tabs = ({ items }) => {
  const [activeTab, setActiveTab] = useState(0);

  const handleTabClick = (index, callback) => {
    setActiveTab(index);
    if (callback) {
      callback();
    }
  };

  return (
    <div className="tabs">
      <div className="tab-headers">
        {items.map((item, index) => (
          <div
            key={index}
            className={`tab-header ${index === activeTab ? 'active' : ''}`}
            onClick={() => handleTabClick(index, item.callback)}
          >
            {item.label}
          </div>
        ))}
      </div>
      <div className="tab-content">
        {items[activeTab] && <div>{items[activeTab].content}</div>}
      </div>
    </div>
  );
};

export default Tabs;
