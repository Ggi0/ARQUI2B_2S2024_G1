import { create } from 'zustand';

const useStore = create((set) => ({
  activeComponent: 'Historico', // Estado inicial
  setActiveComponent: (component) => set({ activeComponent: component }),
}));

export default useStore;