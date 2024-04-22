import React from "react";
import LayoutContent from "../../components/layout/LayoutContent";

/**
 * Layout Container Component
 * Renders the LayoutContent component.
 * Can be extended to include logic for managing layout-specific state or context.
 * @return React.JSX.Element
 */
const LayoutContainer = () => {
  return <LayoutContent />;
};

// Define propTypes if the component starts accepting props in the future
LayoutContainer.propTypes = {};

export default LayoutContainer;
