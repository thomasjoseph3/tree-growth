import * as THREE from "three";
import { gsap } from "gsap";

class GrowingCylinder {
  constructor({
    scene,
    positionY = 0,
    color = 0x8b4513,
    initialHeight = 0.1,
    maxHeight = 50,
    radius = 1,
    growthRate = 0.5,
    initialDirection = new THREE.Vector3(0, 1, 0),
    rotateX = 0,
    rotateZ = 0,
    segments = 32,
    // nextCylinder = [], // Reference to the next cylinder (child) in the chain
  }) {
    this.scene = scene;
    this.maxHeight = maxHeight;
    this.growthRate = growthRate;
    this.direction = initialDirection;
    this.nextCylinders = []; // Child or next cylinder in the sequence
    this.radius = radius;

    // Create a cylinder geometry
    const geometry = new THREE.CylinderGeometry(
      radius * 0.7 * 0.1,
      radius * 0.1,
      initialHeight,
      segments
    );
    geometry.translate(0, initialHeight / 2, 0);
    const material = new THREE.MeshBasicMaterial({
      color,
      roughness: 0.5,
      metalness: 0.1,
    });

    // Create a mesh for the cylinder
    this.cylinder = new THREE.Mesh(geometry, material);
    this.cylinder.visible = false;

    // Create a group to manage positioning and rotation
    this.group = new THREE.Group();
    this.group.add(this.cylinder);

    // Apply the rotation around the X-axis for angled growth
    this.group.rotation.x = THREE.MathUtils.degToRad(rotateX);
    this.group.rotation.z = THREE.MathUtils.degToRad(rotateZ);
    // this.group.rotation.y = THREE.MathUtils.degToRad(20);

    // Set the initial position of the group (cylinder starts from here)
    this.group.position.y = positionY;

    // Add the group to the scene
    this.scene.add(this.group);

    // Create the timeline for animations
    this.timeline = gsap.timeline({ paused: true });
  }

  setNextCylinder(nextCylinder) {
    this.nextCylinders.push(nextCylinder);
  }

  growCylinder(previousCylinder = null) {
    // If there's a previous cylinder, position this cylinder on top of it
    if (previousCylinder) {
      this.setPositionOnTopOf(previousCylinder);
    }

    this.cylinder.visible = true;

    // Animate the cylinder growth
    this.timeline.to(this.cylinder.scale, {
      y: this.maxHeight, // Scale to maxHeight
      // x: this.radius,
      // z: this.radius,
      x: this.radius, // Maintain X scale for bottom
      z: this.radius, // Maintain Z scale for bottom
      duration: 4, // Duration of the animation
      ease: "linear", // Smooth animation
      onUpdate: () => {
        // Use GSAP to dynamically update the position while growing
        this.updatePositionWhileGrowing(previousCylinder);
      },
      onStart: () => {
        // When this cylinder's animation is complete, start the next one if it exists
        for (let nextChild of this.nextCylinders) {
          nextChild.growCylinder(this); // Trigger growth of the next cylinder
        }
      },
    });

    // Start the timeline
    this.timeline.play();
  }

  // Method to dynamically update position while growing
  updatePositionWhileGrowing(bottomCylinder) {
    const currentHeight = this.getCurrentHeight();

    // if (bottomCylinder) {
    //   const bottomHeight = bottomCylinder.getCurrentHeight();

    //   // Manually adjust the Y position
    //   this.group.position.y = bottomCylinder.group.position.y + bottomHeight;
    // } else {
    //   // No bottom cylinder, grow from the base
    //   this.group.position.y = 0;
    // }

    if (bottomCylinder) {
      const bottomHeight = bottomCylinder.getCurrentHeight();

      // Adjust the position dynamically using trigonometry to follow the parent's rotation
      // const rotatedY = bottomCylinder.group.position.y + bottomHeight;

      // // Calculate X and Z based on the parent's rotation
      // const rotatedX =
      //   bottomCylinder.group.position.x +
      //   currentHeight * Math.sin(bottomCylinder.group.rotation.z);
      // const rotatedZ =
      //   bottomCylinder.group.position.z +
      //   currentHeight * Math.sin(bottomCylinder.group.rotation.x);

      this.setPositionOnTopOf(bottomCylinder);
      // Manually adjust the Y, X, and Z position
      // this.group.position.set(rotatedX, rotatedY, rotatedZ);
    } else {
      // No bottom cylinder, grow from the base
      this.group.position.set(0, 0, 0);
    }
  }

  getCurrentHeight() {
    return this.cylinder.scale.y * this.cylinder.geometry.parameters.height;
  }

  getTopPosition() {
    const height = this.getCurrentHeight();
    const localTop = new THREE.Vector3(0, height, 0);
    const worldTop = localTop.clone();
    this.group.localToWorld(worldTop); // Convert local top to world coordinates with rotation

    return worldTop;
  }

  setPositionOnTopOf(previousCylinder) {
    const previousTopPosition = previousCylinder.getTopPosition();
    this.group.position.set(
      previousTopPosition.x,
      previousTopPosition.y - 0.1,
      previousTopPosition.z
    );
  }
}

export default GrowingCylinder;
