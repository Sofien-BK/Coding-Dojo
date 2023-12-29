import React, { useState } from 'react';

const BoxCreator = () => {
  const [color, setColor] = useState('');
  const [boxSize, setBoxSize] = useState({ height: '100px', width: '100px' });
  const [boxes, setBoxes] = useState([]);

  const handleColorChange = (e) => {
    setColor(e.target.value);
  };

  const handleSizeChange = (e) => {
    const newSize = e.target.value;
    setBoxSize({
      height: `${newSize}px`,
      width: `${newSize}px`,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const newBox = {
      color,
      size: { ...boxSize },
    };
    setBoxes([...boxes, newBox]);
    setColor(''); 
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>
          Color:
          <input type="text" value={color} onChange={handleColorChange} />
        </label>
        <label>
          Size:
          <input type="number" value={boxSize.height.slice(0, -2)} onChange={handleSizeChange} />
        </label>
        <button type="submit">Add Box</button>
      </form>

      <div className="box-container">
        {boxes.map((box, index) => (
          <div
            key={index}
            className="box"
            style={{
              backgroundColor: box.color,
              height: box.size.height,
              width: box.size.width,
            }}
          ></div>
        ))}
      </div>
    </div>
  );
};

export default BoxCreator;
