import { StrictMode } from "react";
import { createRoot, Root } from "react-dom/client";
import "./index.css";
import App from "./App";

// Extend the Window type to avoid TypeScript errors
declare global {
  interface Window {
    renderMyWidget: (containerId: string, props?: Record<string, any>) => void;
    unmountMyWidget: (containerId: string) => void;
  }
}

const roots: Record<string, Root> = {};

// Global function to mount the widget
window.renderMyWidget = (containerId, props = {}) => {
  const container = document.getElementById(containerId);
  if (!container) {
    console.error(`Container #${containerId} not found`);
    return;
  }

  if (!roots[containerId]) {
    roots[containerId] = createRoot(container);
  }

  roots[containerId].render(
    <StrictMode>
      <App {...props} />
    </StrictMode>
  );
};

// Global function to unmount the widget
window.unmountMyWidget = (containerId) => {
  if (roots[containerId]) {
    roots[containerId].unmount();
    delete roots[containerId];
  }
};
