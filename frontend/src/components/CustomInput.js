import React from 'react';

const CustomInput = ({ label, value, onChange }) => {
  
  return (
    <div className="flex-grow sm:mr-4">
      <label className="text-lg font-medium text-gray-900">{label}  </label>
      <input
        type="number"
        value={value}
        onChange={onChange}
        className="border border-gray-300 rounded-md px-3 py-2 mt-1 focus:outline-none focus:ring-1 focus:ring-blue-500"
      />
    </div>
  );
};

export default CustomInput;
