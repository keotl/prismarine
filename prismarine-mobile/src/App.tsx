import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import "./App.css";
import { BottomBar } from "./components/BottomBar";
import { Header } from "./components/Header";

import { Player } from "./components/Player";
import { Logo } from "./Logo";
import { AlbumsListView } from "./views/AlbumsListView";
import { AlbumView } from "./views/AlbumView";
import { SettingsView } from "./views/SettingsView";
function App() {
  return (
    <div className="App">
      <Header />
      <BrowserRouter basename={process.env.PUBLIC_URL}>
        <div className="main-content">
          <Routes>
            <Route path="/" element={<Navigate to="/albums" replace />} />

            <Route element={<AlbumsListView />} path="/albums" />
            <Route element={<AlbumView />} path="/albums/:albumId" />
            <Route element={<SettingsView />} path="/settings" />
            <Route element={<Logo />} path="/logo" />
          </Routes>
        </div>
        <Player />
        <BottomBar />
      </BrowserRouter>
    </div>
  );
}

export default App;
