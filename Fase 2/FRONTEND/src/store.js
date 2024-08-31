import { create } from 'zustand';

const useStore = create((set) => ({
  activeComponent: 'Historico', // Estado inicial
  setActiveComponent: (component) => {
    console.log('Changing activeComponent to:', component); // Para debugging
    set({ activeComponent: component });
  },
}));

export default useStore;