import CosmicNarrator from "./components/CosmicNarrator";

export default function App() {
  return (
    <div
      style={{
        backgroundColor: "#000",
        height: "100vh",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        flexDirection: "column",
        padding: "2rem",
      }}
    >
      <h1 style={{ color: "#00ffff", fontFamily: "Orbitron, monospace" }}>
        QubuHub Cosmic Narrator
      </h1>
      <CosmicNarrator />
    </div>
  );
}
