export function formatDuration(floatSeconds) {
  const durationMillis = floatSeconds * 1000;
  const timeInSeconds = Math.floor(durationMillis / 1000);
  const minutes = Math.floor(timeInSeconds / 60);
  const seconds = timeInSeconds - (minutes * 60);
  const formattedSeconds = seconds > 9 ? `${seconds}` : `0${seconds}`;
  return `${minutes}:${formattedSeconds}`;
}
