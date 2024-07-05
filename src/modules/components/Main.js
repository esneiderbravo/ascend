import React, { BrowserRouter, Routes, Route } from 'react-router-dom'
import LayoutContainer from '../containers/layout/LayoutContainer'
import DashboardContainer from '../containers/dashboard/DashboardContainer'
import WithAuth from '../hooks/withAuth'

export default function Main() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<LayoutContainer />} />
        <Route
          path='/dashboard'
          element={
            <WithAuth>
              <DashboardContainer />
            </WithAuth>
          }
        />
      </Routes>
    </BrowserRouter>
  )
}

Main.propTypes = {}
