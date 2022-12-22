export const WORKER_INSTANCE = new Worker(
  new URL("./workerMain.ts", import.meta.url)
);
WORKER_INSTANCE.postMessage({ command: "initialize" });
