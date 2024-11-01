import React, { useEffect } from "react";
import Manager from "./TreeManager";

const GenerateTree = () => {
  useEffect(() => {
    const manager = new Manager();
    manager.init("tree-viewer");
    // manager.addCubeToScene();
  }, []);
  return <div id="tree-viewer"></div>;
};

export default GenerateTree;
