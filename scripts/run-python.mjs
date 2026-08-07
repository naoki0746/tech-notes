import { existsSync } from "node:fs";
import { spawnSync } from "node:child_process";
import path from "node:path";
import os from "node:os";

const args = process.argv.slice(2);
const candidates = [
  process.env.PYTHON ? [process.env.PYTHON] : null,
  ["python"],
  ["python3"],
  ["py", "-3"],
  [path.join(os.homedir(), ".cache", "codex-runtimes", "codex-primary-runtime", "dependencies", "python", "python.exe")]
].filter(Boolean);

for (const candidate of candidates) {
  const [command, ...prefixArgs] = candidate;
  if (command.includes(path.sep) && !existsSync(command)) {
    continue;
  }

  const probe = spawnSync(command, [...prefixArgs, "--version"], {
    stdio: "ignore",
    shell: false
  });

  if (probe.error || probe.status !== 0) {
    continue;
  }

  const result = spawnSync(command, [...prefixArgs, ...args], {
    stdio: "inherit",
    shell: false
  });

  if (result.error) {
    console.error(result.error.message);
    process.exit(1);
  }

  process.exit(result.status ?? 0);
}

console.error("Python was not found. Install Python 3 or set the PYTHON environment variable.");
process.exit(1);
