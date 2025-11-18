export function formatBytes(bytes: number, decimals: number = 2): string {
  // BUGFIX: Handle edge cases for negative numbers and NaN
  if (bytes === 0) return '0 Bytes';
  if (bytes < 0) return '0 Bytes'; // Handle negative bytes
  if (!Number.isFinite(bytes)) return '0 Bytes'; // Handle NaN and Infinity

  const k = 1024;
  // BUGFIX: Limit decimals to reasonable range
  const dm = Math.max(0, Math.min(decimals, 10));
  const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB'];

  const i = Math.floor(Math.log(bytes) / Math.log(k));

  // BUGFIX: Prevent array bounds overflow
  const sizeIndex = Math.min(i, sizes.length - 1);

  return parseFloat((bytes / Math.pow(k, sizeIndex)).toFixed(dm)) + ' ' + sizes[sizeIndex];
}
