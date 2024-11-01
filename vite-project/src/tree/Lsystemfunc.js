const lSystemRules = {
    "F": "F[+F][-F]"
  };
  const axiom = "F";
  let iterations = 4;
  function generateLSystem(axiom, rules, iterations) {
    let current = axiom;
    for (let i = 0; i < iterations; i++) {
      let next = "";
      for (let char of current) {
        next += rules[char] || char;
      }
      current = next;
    }
    return current;
  }
  

  
  export {lSystemRules,generateLSystem}