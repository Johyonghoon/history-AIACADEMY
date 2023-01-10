import * as React from 'react';
import Box from '@mui/material/Box';
import BottomNavigation from '@mui/material/BottomNavigation';
import { Link } from "react-router-dom"

const Navigation = () => {
  const [value, setValue] = React.useState(0);

  return (
    <Box sx={{ width: 1200 }}>
      <BottomNavigation
        showLabels
        value={value}
        onChange={(event, newValue) => {
          setValue(newValue);
        }}
      >
        <Link to="/home" style={{width:50, margin:10}}>Home</Link>
        <Link to="/counter" style={{width:50, margin:10}}>Counter</Link>
        <Link to="/todos" style={{width:50, margin:10}}>Todos</Link>
        <Link to="/dummy" style={{width:60, margin:10}}>Dummy Accounts</Link>
        <Link to="/login" style={{width:50, margin:10}}>Login</Link>
        <Link to="/list" style={{width:50, margin:10}}>User List</Link>
        <Link to="/stroke" style={{width:50, margin:10}}>Stroke</Link>
        <Link to="/iris" style={{width:50, margin:10}}>Iris</Link>
        <Link to="/fashion" style={{width:50, margin:10}}>Fashion</Link>
        <Link to="/mnist" style={{width:50, margin:10}}>MNIST</Link>
        <Link to="/naver-movie" style={{width:100, margin:10}}>WebCrawler</Link>
        <Link to="/samsung-report" style={{width:100, margin:10}}>samsung-report</Link>
        <Link to="/imdb" style={{width:50, margin:10}}>IMDb</Link>
        <Link to="/aitrader" style={{width:50, margin:10}}>AITrader</Link>
      </BottomNavigation>
    </Box>
  );
}

export default Navigation
