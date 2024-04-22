import React from "react";
import DashboardContent from "../../components/dashboard/DashboardContent";

/**
 * DashboardContainer Component
 * Renders the DashboardContent component.
 * Can be extended to include logic for fetching data or handling user interactions.
 * @return React.JSX.Element
 */
const DashboardContainer = () => {
  return <DashboardContent />;
};

// Define propTypes if the component starts accepting props in the future
DashboardContainer.propTypes = {};

export default DashboardContainer;
