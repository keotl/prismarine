import { useContext, useEffect, useState } from "react";
import { HeaderContext } from "../context/HeaderContext";
import { SavedMediaContext } from "../context/SavedMediaContext";
import { WORKER_INSTANCE } from "../worker/worker";
import styles from "./SettingsView.module.css";

export function SettingsView() {
  const header = useContext(HeaderContext);
  const savedMedia = useContext(SavedMediaContext);

  useEffect(() => {
    header.update({
      visible: true,
      title: "Settings",
      action: undefined,
      showBack: true,
    });
  }, [header.update]);

  const [message, setMessage] = useState("");

  return (
    <div className={styles.container}>
      <div
        className={styles.button}
        onClick={() => {
          WORKER_INSTANCE.postMessage({ command: "updateLibraryMetadata" });
          setMessage(
            "Database refresh is running in the background. Wait a few minutes before refreshing the page."
          );
        }}
      >
        Refresh library
      </div>
      <div
        className={styles.button}
        onClick={() => {
          const request = indexedDB.deleteDatabase("cache");
          savedMedia.close();
          WORKER_INSTANCE.postMessage({ command: "closeDb" });
          request.onsuccess = () => {
            console.log("successfully deleted db cache");
            window.location.reload();
          };
        }}
      >
        Destroy database
      </div>
      <div
        className={styles.button}
        onClick={() => window.location.replace(process.env.PUBLIC_URL + "?")}
      >
        Refresh page
      </div>

      {message}
    </div>
  );
}
