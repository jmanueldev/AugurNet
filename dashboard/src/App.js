import React, { useEffect, useState } from "react";
import axios from "axios";
import ForceGraph2D from "react-force-graph-2d";

function App() {
  const [graph, setGraph] = useState({ nodes: [], links: [] });

  useEffect(() => {
    axios.get("http://localhost:8000/graph").then(res => {
      setGraph(res.data);
    });
  }, []);

  return (
    <div>
      <h2>AugurNet Causal Graph</h2>
      <ForceGraph2D
        graphData={graph}
        nodeLabel="id"
        linkDirectionalArrowLength={5}
      />
    </div>
  );
}

export default App;