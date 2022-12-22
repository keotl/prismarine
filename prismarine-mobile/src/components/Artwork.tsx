import styles from "./Artwork.module.css";

type Props = {
  imageUrl: string | null;
  size?: number;
};

export function Artwork({ imageUrl, size }: Props) {
  return (
    <>
      {imageUrl ? (
        <img
          className={styles.thumbnail}
          style={{ height: size }}
          src={imageUrl}
        />
      ) : (
        <div
          className={styles.thumbnail + " " + styles.placeholder}
          style={{ width: size, height: size }}
        >
          <span className="material-symbols-rounded">music_note</span>
        </div>
      )}
    </>
  );
}
