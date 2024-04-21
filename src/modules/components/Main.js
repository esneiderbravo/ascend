import { BrowserRouter, Routes, Route } from "react-router-dom";
import LayoutContainer from "../containers/layout/LayoutContainer";
import DashboardContainer from "../containers/dashboard/DashboardContainer";

export default function Main() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<LayoutContainer />} />
        <Route path="/dashboard" element={<DashboardContainer />} />
      </Routes>
    </BrowserRouter>
  );
}

Main.propTypes = {};
