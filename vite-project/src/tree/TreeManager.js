import * as THREE from "three";
import CameraControls from "camera-controls";
import GrowingCylinder from "./GrowingCylinder2";
import { gsap } from "gsap";

CameraControls.install({ THREE });

class TreeManager {
  constructor() {
    this.container = null;
    this.scene = null;
    this.camera = null;
    this.renderer = null;
    this.controls = null;
    this.clock = new THREE.Clock();
    this.animateArr = [];
  }

  init(tagId) {
    // Scene setup
    this.scene = new THREE.Scene();
    this.scene.add(new THREE.AxesHelper(1)); // Add axes helper to visualize orientation

    // Camera setup
    this.camera = new THREE.PerspectiveCamera(
      75,
      window.innerWidth / window.innerHeight,
      0.1,
      1000
    );
    this.camera.position.set(5, 10, 15); // Move the camera closer to the tree

    // Light setup
    this.spotLight = new THREE.SpotLight(0xffffff, 50); // Increased intensity significantly
    this.spotLight.position.set(50, 50, 50);
    this.spotLight.castShadow = true; // Enable shadows for the spotlight
    this.spotLight.shadow.mapSize.width = 4096; // Higher resolution for better shadow quality
    this.spotLight.shadow.mapSize.height = 4096;
    this.spotLight.angle = Math.PI / 3; // Widen the beam angle to cover more area
    this.spotLight.penumbra = 0.2; // Add slight softness to shadows
    this.spotLight.shadow.camera.near = 1;
    this.spotLight.shadow.camera.far = 500;
    this.spotLight.shadow.bias = -0.001;
    this.scene.add(this.spotLight);

    this.followLight = new THREE.DirectionalLight(0xffffff, 3);
    this.followLight.position.copy(this.camera.position);
    this.scene.add(this.followLight);

    const ambientLight = new THREE.AmbientLight(0xffffff, 0.5); // Soft ambient light
    this.scene.add(ambientLight);

    // Renderer setup
    this.renderer = new THREE.WebGLRenderer({ antialias: true });
    this.renderer.setSize(window.innerWidth, window.innerHeight);
    this.renderer.shadowMap.enabled = true;
    this.container = document.getElementById(tagId);
    this.container.appendChild(this.renderer.domElement);

    // Camera controls
    this.controls = new CameraControls(this.camera, this.renderer.domElement);
    this.controls.dampingFactor = 0.25;
    this.controls.draggingDampingFactor = 0.25;
    this.controls.minDistance = 1;
    this.controls.maxDistance = 50;
    this.controls.dollyToCursor = true;

    const resizeUnsubscribe = this.initResize();
    const unmountElement = () => {
      this.container.removeChild(this.renderer.domElement);
    };

    this.animate();

    // this.animateCylinder();
    this.animateCylinder2();

    return () => {
      resizeUnsubscribe();
      unmountElement();
    };
  }

  addCubeToScene() {
    const geometry = new THREE.BoxGeometry(10, 10, 10);
    const material = new THREE.MeshStandardMaterial({
      color: 0x0055ff,
      roughness: 0.5,
      metalness: 0.1,
    });

    const cube = new THREE.Mesh(geometry, material);
    cube.castShadow = true;
    cube.receiveShadow = true;
    cube.position.set(0, 0, 0);
    this.scene.add(cube);
    this.camera.lookAt(cube.position);
  }

  animateCylinder() {
    const growingCylinder1 = new GrowingCylinder({ scene: this.scene });
    const growingCylinder2 = new GrowingCylinder({
      scene: this.scene,
      positionY: growingCylinder1.getCurrentHeight(),
      color: 0x8b4513,
      angle: 30,
      radius: 0.5,
    });
    this.animateArr.push(() => {
      growingCylinder1.animate();
      growingCylinder2.animate(growingCylinder1);
    });
  }

  animateCylinder2() {
    const growingCylinder1 = new GrowingCylinder({
      scene: this.scene,
      radius: 2.5,
    });

    const growingCylinder2 = new GrowingCylinder({
      scene: this.scene,
      // positionY: 5,
      initialHeight: 0.1,
      maxHeight: 40,
      radius: 2,
      // color: 0xff22ff,
      // rotateX: 50,
      rotateZ: 50,
    });
    const growingCylinder3 = new GrowingCylinder({
      scene: this.scene,
      // positionY: 5,
      initialHeight: 0.1,
      maxHeight: 35,
      radius: 2,
      // color: 0xff22ff,
      // rotateX: -20,
      rotateZ: -20,
      rotateX: -20,
    });
    const growingCylinder4 = new GrowingCylinder({
      scene: this.scene,
      // positionY: 5,
      initialHeight: 0.1,
      maxHeight: 20,
      radius: 1.3,
      // color: 0xff22ff,
      rotateX: 20,
    });
    const growingCylinder5 = new GrowingCylinder({
      scene: this.scene,
      // positionY: 5,
      initialHeight: 0.1,
      maxHeight: 20,
      radius: 1.3,
      // color: 0xff22ff,
      rotateX: -10,
      rotateZ: 0,
    });
    const growingCylinder6 = new GrowingCylinder({
      scene: this.scene,
      // positionY: 5,
      initialHeight: 0.1,
      maxHeight: 20,
      radius: 1.3,
      // color: 0xff22ff,
      rotateX: 10,
    });
    const growingCylinder7 = new GrowingCylinder({
      scene: this.scene,
      // positionY: 5,
      initialHeight: 0.1,
      maxHeight: 20,
      radius: 1.3,
      // color: 0xff22ff,
      rotateX: 0,
      rotateZ: 20,
    });

    growingCylinder1.setNextCylinder(growingCylinder2);
    growingCylinder1.setNextCylinder(growingCylinder3);
    growingCylinder2.setNextCylinder(growingCylinder4);
    growingCylinder2.setNextCylinder(growingCylinder5);
    growingCylinder3.setNextCylinder(growingCylinder6);
    growingCylinder3.setNextCylinder(growingCylinder7);

    growingCylinder1.growCylinder();

    // // Trigger the cylinder growth animation using GSAP
    // growingCylinder1.growCylinder();
    // // growingCylinder2.growCylinder(5);

    // // Align the second cylinder on top of the first after it grows
    // gsap.delayedCall(1, () => {
    //   growingCylinder2.growCylinder(growingCylinder1);
    //   growingCylinder3.growCylinder(growingCylinder1);

    //   gsap.delayedCall(1, () => {
    //     growingCylinder4.growCylinder(growingCylinder2);
    //     growingCylinder5.growCylinder(growingCylinder2);

    //     growingCylinder6.growCylinder(growingCylinder3);
    //     growingCylinder7.growCylinder(growingCylinder3);
    //   });
    // });
  }

  animate = () => {
    window.requestAnimationFrame(this.animate);

    if (this.camera.position) {
      this.followLight.position.copy(this.camera.position);
    }
    if (this.controls.target) {
      this.followLight.target.position.copy(this.controls.target);
    }

    const delta = this.clock.getDelta();
    this.controls?.update(delta);

    for (let animateItems of this.animateArr) {
      animateItems();
    }

    this.render();
  };

  render() {
    this.renderer.render(this.scene, this.camera);
  }

  initResize = () => {
    const onWindowResize = () => {
      this.camera.aspect = window.innerWidth / window.innerHeight;
      this.camera.updateProjectionMatrix();
      this.renderer.setSize(window.innerWidth, window.innerHeight);
      this.render();
    };
    window.addEventListener("resize", onWindowResize.bind(this));

    return () => {
      window.removeEventListener("resize", onWindowResize.bind(this));
    };
  };
}

export default TreeManager;
