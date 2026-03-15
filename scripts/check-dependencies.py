#!/usr/bin/env python3
"""
Cross-platform dependency checker and installer for ai_collection project.

Usage:
    python scripts/check-dependencies.py              # Check all dependencies
    python scripts/check-dependencies.py --install    # Auto-install missing deps
    python scripts/check-dependencies.py --skill akshare  # Check specific skill
    python scripts/check-dependencies.py --report     # Generate JSON report
"""

import argparse
import json
import platform
import shutil
import subprocess
import sys
import re
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Optional


# ============================================================================
# Color Output
# ============================================================================

class Colors:
    """ANSI color codes for terminal output."""
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RESET = '\033[0m'

    @classmethod
    def disable(cls):
        """Disable colors (for non-TTY output)."""
        cls.RED = cls.GREEN = cls.YELLOW = cls.BLUE = ''
        cls.MAGENTA = cls.CYAN = cls.WHITE = cls.BOLD = cls.DIM = cls.RESET = ''


def colorize(text: str, color: str) -> str:
    """Apply color to text."""
    return f"{color}{text}{Colors.RESET}"


def print_success(msg: str):
    print(f"{Colors.GREEN}✅ {msg}{Colors.RESET}")


def print_error(msg: str):
    print(f"{Colors.RED}❌ {msg}{Colors.RESET}")


def print_warning(msg: str):
    print(f"{Colors.YELLOW}⚠️  {msg}{Colors.RESET}")


def print_info(msg: str):
    print(f"{Colors.BLUE}ℹ️  {msg}{Colors.RESET}")


def print_header(msg: str):
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'=' * 60}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}  {msg}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'=' * 60}{Colors.RESET}\n")


# ============================================================================
# System Detection
# ============================================================================

class OSType(Enum):
    MACOS = "macos"
    LINUX_DEBIAN = "linux_debian"
    LINUX_REDHAT = "linux_redhat"
    LINUX_ARCH = "linux_arch"
    WINDOWS = "windows"
    UNKNOWN = "unknown"


@dataclass
class SystemInfo:
    """Detected system information."""
    os_type: OSType
    os_name: str
    os_version: str
    arch: str
    package_manager: str
    install_commands: dict


def detect_system() -> SystemInfo:
    """Detect the current operating system and package manager."""
    system = platform.system().lower()
    machine = platform.machine().lower()
    
    if system == "darwin":
        return SystemInfo(
            os_type=OSType.MACOS,
            os_name="macOS",
            os_version=platform.mac_ver()[0],
            arch=machine,
            package_manager="brew",
            install_commands={
                "brew": "brew install {package}",
                "pip": "pip3 install {package}",
                "npm": "npm install -g {package}",
            }
        )
    
    elif system == "linux":
        # Detect Linux distribution
        distro_info = _detect_linux_distro()
        return SystemInfo(
            os_type=distro_info["type"],
            os_name=distro_info["name"],
            os_version=distro_info["version"],
            arch=machine,
            package_manager=distro_info["package_manager"],
            install_commands=distro_info["install_commands"],
        )
    
    elif system == "windows":
        return SystemInfo(
            os_type=OSType.WINDOWS,
            os_name="Windows",
            os_version=platform.version(),
            arch=machine,
            package_manager="winget",
            install_commands={
                "winget": "winget install {package}",
                "scoop": "scoop install {package}",
                "choco": "choco install {package}",
                "pip": "pip install {package}",
                "npm": "npm install -g {package}",
            }
        )
    
    else:
        return SystemInfo(
            os_type=OSType.UNKNOWN,
            os_name=system.capitalize(),
            os_version=platform.version(),
            arch=machine,
            package_manager="unknown",
            install_commands={},
        )


def _detect_linux_distro() -> dict:
    """Detect Linux distribution."""
    # Try os-release first
    os_release = Path("/etc/os-release")
    if os_release.exists():
        content = os_release.read_text()
        info = {}
        for line in content.splitlines():
            if "=" in line:
                key, value = line.split("=", 1)
                info[key] = value.strip('"')
        
        distro_id = info.get("ID", "").lower()
        distro_name = info.get("NAME", "Linux")
        distro_version = info.get("VERSION_ID", "")
        
        # Debian-based
        if distro_id in ("debian", "ubuntu", "linuxmint", "pop", "elementary", "kali"):
            return {
                "type": OSType.LINUX_DEBIAN,
                "name": distro_name,
                "version": distro_version,
                "package_manager": "apt",
                "install_commands": {
                    "apt": "sudo apt install -y {package}",
                    "pip": "pip3 install {package}",
                    "npm": "npm install -g {package}",
                }
            }
        
        # RedHat-based
        elif distro_id in ("fedora", "rhel", "centos", "rocky", "almalinux", "ol"):
            pm = "dnf" if shutil.which("dnf") else "yum"
            return {
                "type": OSType.LINUX_REDHAT,
                "name": distro_name,
                "version": distro_version,
                "package_manager": pm,
                "install_commands": {
                    "dnf": "sudo dnf install -y {package}",
                    "yum": "sudo yum install -y {package}",
                    "pip": "pip3 install {package}",
                    "npm": "npm install -g {package}",
                }
            }
        
        # Arch-based
        elif distro_id in ("arch", "manjaro", "endeavouros"):
            return {
                "type": OSType.LINUX_ARCH,
                "name": distro_name,
                "version": distro_version,
                "package_manager": "pacman",
                "install_commands": {
                    "pacman": "sudo pacman -S --noconfirm {package}",
                    "pip": "pip3 install {package}",
                    "npm": "npm install -g {package}",
                }
            }
    
    # Fallback: check for package managers
    if shutil.which("apt"):
        return {
            "type": OSType.LINUX_DEBIAN,
            "name": "Linux (Debian-based)",
            "version": "",
            "package_manager": "apt",
            "install_commands": {
                "apt": "sudo apt install -y {package}",
                "pip": "pip3 install {package}",
                "npm": "npm install -g {package}",
            }
        }
    elif shutil.which("dnf"):
        return {
            "type": OSType.LINUX_REDHAT,
            "name": "Linux (RedHat-based)",
            "version": "",
            "package_manager": "dnf",
            "install_commands": {
                "dnf": "sudo dnf install -y {package}",
                "pip": "pip3 install {package}",
                "npm": "npm install -g {package}",
            }
        }
    elif shutil.which("yum"):
        return {
            "type": OSType.LINUX_REDHAT,
            "name": "Linux (RedHat-based)",
            "version": "",
            "package_manager": "yum",
            "install_commands": {
                "yum": "sudo yum install -y {package}",
                "pip": "pip3 install {package}",
                "npm": "npm install -g {package}",
            }
        }
    elif shutil.which("pacman"):
        return {
            "type": OSType.LINUX_ARCH,
            "name": "Linux (Arch-based)",
            "version": "",
            "package_manager": "pacman",
            "install_commands": {
                "pacman": "sudo pacman -S --noconfirm {package}",
                "pip": "pip3 install {package}",
                "npm": "npm install -g {package}",
            }
        }
    
    return {
        "type": OSType.UNKNOWN,
        "name": "Linux",
        "version": "",
        "package_manager": "unknown",
        "install_commands": {
            "pip": "pip3 install {package}",
            "npm": "npm install -g {package}",
        }
    }


# ============================================================================
# Dependency Definitions
# ============================================================================

@dataclass
class Dependency:
    """Represents a single dependency."""
    name: str
    version_required: Optional[str] = None
    version_installed: Optional[str] = None
    installed: bool = False
    optional: bool = False
    category: str = "system"  # system, python, npm
    install_cmd: Optional[str] = None
    check_cmd: Optional[str] = None


@dataclass
class Skill:
    """Represents a skill with its dependencies."""
    name: str
    description: str
    dependencies: list[Dependency] = field(default_factory=list)
    package_files: list[str] = field(default_factory=list)


# Define skills and their dependencies
SKILLS: dict[str, Skill] = {
    "chat-history-lancedb": Skill(
        name="chat-history-lancedb",
        description="LanceDB-based chat history with vector search",
        package_files=["package.json"],
        dependencies=[
            Dependency(name="node", version_required=">=20.0.0", category="system"),
            Dependency(name="npm", category="system"),
        ]
    ),
    "skill-rag-indexer": Skill(
        name="skill-rag-indexer",
        description="RAG indexer for local skill documents",
        package_files=["package.json"],
        dependencies=[
            Dependency(name="node", version_required=">=20.0.0", category="system"),
            Dependency(name="npm", category="system"),
        ]
    ),
    "akshare": Skill(
        name="akshare",
        description="Chinese financial market data access",
        dependencies=[
            Dependency(name="python3", version_required=">=3.8", category="system"),
            Dependency(name="pip3", category="system"),
            Dependency(name="akshare", category="python"),
        ]
    ),
    "stock-analysis": Skill(
        name="stock-analysis",
        description="Comprehensive stock technical analysis",
        dependencies=[
            Dependency(name="python3", version_required=">=3.8", category="system"),
            Dependency(name="pip3", category="system"),
            Dependency(name="akshare", category="python"),
            Dependency(name="pandas", category="python"),
            Dependency(name="numpy", category="python"),
            Dependency(name="matplotlib", category="python"),
            Dependency(name="plotly", category="python"),
            Dependency(name="TA-Lib", category="python", optional=True),
            Dependency(name="mplfinance", category="python", optional=True),
            Dependency(name="scikit-learn", category="python", optional=True),
        ]
    ),
    "teach-cofounder": Skill(
        name="teach-cofounder",
        description="Socratic technical mentorship framework",
        dependencies=[]  # No external dependencies
    ),
}

# System tool mappings for different OS
SYSTEM_PACKAGES = {
    OSType.MACOS: {
        "python3": {"brew": "python@3.12", "check": "python3 --version"},
        "pip3": {"brew": "python@3.12", "check": "pip3 --version"},
        "node": {"brew": "node", "check": "node --version"},
        "npm": {"brew": "node", "check": "npm --version"},
        "git": {"brew": "git", "check": "git --version"},
    },
    OSType.LINUX_DEBIAN: {
        "python3": {"apt": "python3", "check": "python3 --version"},
        "pip3": {"apt": "python3-pip", "check": "pip3 --version"},
        "node": {"apt": "nodejs", "check": "node --version"},
        "npm": {"apt": "npm", "check": "npm --version"},
        "git": {"apt": "git", "check": "git --version"},
    },
    OSType.LINUX_REDHAT: {
        "python3": {"dnf": "python3", "yum": "python3", "check": "python3 --version"},
        "pip3": {"dnf": "python3-pip", "yum": "python3-pip", "check": "pip3 --version"},
        "node": {"dnf": "nodejs", "yum": "nodejs", "check": "node --version"},
        "npm": {"dnf": "npm", "yum": "npm", "check": "npm --version"},
        "git": {"dnf": "git", "yum": "git", "check": "git --version"},
    },
    OSType.LINUX_ARCH: {
        "python3": {"pacman": "python", "check": "python --version"},
        "pip3": {"pacman": "python-pip", "check": "pip --version"},
        "node": {"pacman": "nodejs", "check": "node --version"},
        "npm": {"pacman": "npm", "check": "npm --version"},
        "git": {"pacman": "git", "check": "git --version"},
    },
    OSType.WINDOWS: {
        "python3": {"winget": "Python.Python.3.12", "choco": "python", "check": "python --version"},
        "pip3": {"winget": "Python.Python.3.12", "choco": "python", "check": "pip --version"},
        "node": {"winget": "OpenJS.NodeJS.LTS", "choco": "nodejs", "check": "node --version"},
        "npm": {"winget": "OpenJS.NodeJS.LTS", "choco": "nodejs", "check": "npm --version"},
        "git": {"winget": "Git.Git", "choco": "git", "check": "git --version"},
    },
}


# ============================================================================
# Dependency Checking
# ============================================================================

def check_command_exists(cmd: str) -> bool:
    """Check if a command exists in PATH."""
    return shutil.which(cmd) is not None


def get_command_version(cmd: str, version_flag: str = "--version") -> Optional[str]:
    """Get the version of a command."""
    try:
        result = subprocess.run(
            [cmd, version_flag],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            # Extract version number from output
            output = result.stdout.strip() or result.stderr.strip()
            # Common version patterns
            match = re.search(r'(\d+\.\d+\.\d+|\d+\.\d+)', output)
            if match:
                return match.group(1)
        return None
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return None


def compare_versions(version1: str, version2: str) -> int:
    """Compare two version strings. Returns -1, 0, or 1."""
    def parse_version(v):
        return [int(x) for x in v.split('.')]
    
    v1_parts = parse_version(version1)
    v2_parts = parse_version(version2)
    
    # Pad shorter version
    max_len = max(len(v1_parts), len(v2_parts))
    v1_parts += [0] * (max_len - len(v1_parts))
    v2_parts += [0] * (max_len - len(v2_parts))
    
    for a, b in zip(v1_parts, v2_parts):
        if a < b:
            return -1
        if a > b:
            return 1
    return 0


def check_python_package(package: str) -> tuple[bool, Optional[str]]:
    """Check if a Python package is installed."""
    try:
        result = subprocess.run(
            ["pip3", "show", package],
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode == 0:
            # Extract version
            match = re.search(r'Version:\s*(\S+)', result.stdout)
            version = match.group(1) if match else None
            return True, version
        return False, None
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return False, None


def check_npm_package(package: str) -> tuple[bool, Optional[str]]:
    """Check if an npm package is installed globally."""
    try:
        result = subprocess.run(
            ["npm", "list", "-g", package, "--depth=0"],
            capture_output=True,
            text=True,
            timeout=30
        )
        if package in result.stdout:
            match = re.search(rf'{package}@(\d+\.\d+\.\d+)', result.stdout)
            version = match.group(1) if match else None
            return True, version
        return False, None
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return False, None


def check_dependency(dep: Dependency, system: SystemInfo) -> Dependency:
    """Check if a dependency is installed and get its version."""
    if dep.category == "system":
        # System tools
        cmd = dep.name.replace("3", "") if dep.name in ("python3", "pip3") else dep.name
        if check_command_exists(dep.name):
            dep.installed = True
            dep.version_installed = get_command_version(dep.name)
        elif check_command_exists(cmd):
            dep.installed = True
            dep.version_installed = get_command_version(cmd)
    
    elif dep.category == "python":
        installed, version = check_python_package(dep.name)
        dep.installed = installed
        dep.version_installed = version
    
    elif dep.category == "npm":
        installed, version = check_npm_package(dep.name)
        dep.installed = installed
        dep.version_installed = version
    
    # Check version requirement
    if dep.installed and dep.version_required and dep.version_installed:
        # Parse requirement (e.g., ">=3.8")
        req_match = re.match(r'([><=!]+)(\d+\.\d+(?:\.\d+)?)', dep.version_required)
        if req_match:
            op, req_ver = req_match.groups()
            cmp = compare_versions(dep.version_installed, req_ver)
            
            if op == ">=":
                dep.installed = cmp >= 0
            elif op == ">":
                dep.installed = cmp > 0
            elif op == "==":
                dep.installed = cmp == 0
            elif op == "<=":
                dep.installed = cmp <= 0
            elif op == "<":
                dep.installed = cmp < 0
    
    return dep


def check_skill(skill: Skill, system: SystemInfo) -> Skill:
    """Check all dependencies for a skill."""
    skill.dependencies = [
        check_dependency(dep, system) for dep in skill.dependencies
    ]
    return skill


# ============================================================================
# Installation
# ============================================================================

def get_install_command(dep: Dependency, system: SystemInfo) -> Optional[str]:
    """Get the install command for a dependency."""
    if dep.category == "system":
        packages = SYSTEM_PACKAGES.get(system.os_type, {})
        if dep.name in packages:
            pkg_info = packages[dep.name]
            # Use the appropriate package manager
            pm = system.package_manager
            if pm in pkg_info:
                package_name = pkg_info[pm]
                return system.install_commands.get(pm, "").format(package=package_name)
    
    elif dep.category == "python":
        return system.install_commands.get("pip", "pip3 install {package}").format(package=dep.name)
    
    elif dep.category == "npm":
        return system.install_commands.get("npm", "npm install -g {package}").format(package=dep.name)
    
    return None


def install_dependency(dep: Dependency, system: SystemInfo, dry_run: bool = False) -> bool:
    """Install a dependency."""
    cmd = get_install_command(dep, system)
    
    if not cmd:
        print_warning(f"No install command available for {dep.name} on {system.os_name}")
        return False
    
    if dry_run:
        print_info(f"[dry-run] Would run: {cmd}")
        return True
    
    print_info(f"Installing {dep.name}...")
    print_info(f"Running: {cmd}")
    
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            timeout=300  # 5 minutes timeout
        )
        
        if result.returncode == 0:
            print_success(f"Successfully installed {dep.name}")
            return True
        
        # Check for externally-managed-environment error
        if "externally-managed-environment" in result.stderr or "--break-system-packages" in result.stderr:
            print_warning("System Python is externally managed. Trying alternative methods...")
            
            # Try with --break-system-packages flag
            alt_cmd = cmd.replace("pip3 install", "pip3 install --break-system-packages")
            print_info(f"Trying: {alt_cmd}")
            
            result2 = subprocess.run(
                alt_cmd,
                shell=True,
                capture_output=True,
                text=True,
                timeout=300
            )
            
            if result2.returncode == 0:
                print_success(f"Successfully installed {dep.name} (with --break-system-packages)")
                return True
            else:
                print_error(f"Failed to install {dep.name}: {result2.stderr}")
                print_info("Consider using a virtual environment or pipx for Python packages.")
                return False
        
        print_error(f"Failed to install {dep.name}: {result.stderr}")
        return False
    
    except subprocess.TimeoutExpired:
        print_error(f"Installation timed out for {dep.name}")
        return False
    except Exception as e:
        print_error(f"Error installing {dep.name}: {e}")
        return False


# ============================================================================
# Output & Reporting
# ============================================================================

def print_system_info(system: SystemInfo):
    """Print detected system information."""
    print_header("System Information")
    print(f"  {Colors.BOLD}OS:{Colors.RESET}        {system.os_name}")
    print(f"  {Colors.BOLD}Version:{Colors.RESET}   {system.os_version}")
    print(f"  {Colors.BOLD}Architecture:{Colors.RESET} {system.arch}")
    print(f"  {Colors.BOLD}Package Manager:{Colors.RESET} {system.package_manager}")


def print_dependency_status(dep: Dependency):
    """Print the status of a single dependency."""
    status_icon = "✅" if dep.installed else ("⚠️ " if dep.optional else "❌")
    status_color = Colors.GREEN if dep.installed else (Colors.YELLOW if dep.optional else Colors.RED)
    
    version_info = f" ({dep.version_installed})" if dep.version_installed else ""
    req_info = f" [required: {dep.version_required}]" if dep.version_required and not dep.installed else ""
    
    print(f"    {status_color}{status_icon} {dep.name}{Colors.RESET}{version_info}{req_info}")


def print_skill_status(skill: Skill):
    """Print the status of a skill's dependencies."""
    print(f"\n  {Colors.BOLD}{Colors.MAGENTA}{skill.name}:{Colors.RESET}")
    print(f"    {Colors.DIM}{skill.description}{Colors.RESET}")
    
    if not skill.dependencies:
        print(f"    {Colors.GREEN}✅ No external dependencies{Colors.RESET}")
        return
    
    for dep in skill.dependencies:
        print_dependency_status(dep)


def generate_report(skills: list[Skill], system: SystemInfo) -> dict:
    """Generate a JSON report of dependency status."""
    total_deps = 0
    satisfied_deps = 0
    missing_required = []
    missing_optional = []
    
    skills_report = {}
    
    for skill in skills:
        skill_report = {
            "name": skill.name,
            "description": skill.description,
            "satisfied": True,
            "dependencies": []
        }
        
        for dep in skill.dependencies:
            total_deps += 1
            if dep.installed:
                satisfied_deps += 1
            
            dep_report = {
                "name": dep.name,
                "installed": dep.installed,
                "version_installed": dep.version_installed,
                "version_required": dep.version_required,
                "optional": dep.optional,
                "category": dep.category,
            }
            
            skill_report["dependencies"].append(dep_report)
            
            if not dep.installed:
                if dep.optional:
                    missing_optional.append(f"{skill.name}/{dep.name}")
                else:
                    missing_required.append(f"{skill.name}/{dep.name}")
                    skill_report["satisfied"] = False
        
        skills_report[skill.name] = skill_report
    
    return {
        "system": {
            "os": system.os_name,
            "version": system.os_version,
            "architecture": system.arch,
            "package_manager": system.package_manager,
        },
        "summary": {
            "total_dependencies": total_deps,
            "satisfied": satisfied_deps,
            "missing_required": len(missing_required),
            "missing_optional": len(missing_optional),
            "satisfaction_rate": f"{satisfied_deps}/{total_deps}",
        },
        "missing": {
            "required": missing_required,
            "optional": missing_optional,
        },
        "skills": skills_report,
    }


# ============================================================================
# Main
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Cross-platform dependency checker for ai_collection",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/check-dependencies.py              # Check all dependencies
  python scripts/check-dependencies.py --install    # Auto-install missing deps
  python scripts/check-dependencies.py --skill akshare  # Check specific skill
  python scripts/check-dependencies.py --report     # Generate JSON report
        """
    )
    parser.add_argument(
        "--install",
        action="store_true",
        help="Auto-install missing dependencies"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be installed without actually installing"
    )
    parser.add_argument(
        "--skill",
        type=str,
        help="Check a specific skill's dependencies"
    )
    parser.add_argument(
        "--report",
        action="store_true",
        help="Generate JSON report"
    )
    parser.add_argument(
        "--no-color",
        action="store_true",
        help="Disable colored output"
    )
    
    args = parser.parse_args()
    
    # Disable colors if requested or if not a TTY
    if args.no_color or not sys.stdout.isatty():
        Colors.disable()
    
    # Detect system
    system = detect_system()
    
    # Print system info
    print_system_info(system)
    
    # Select skills to check
    if args.skill:
        if args.skill in SKILLS:
            skills_to_check = [SKILLS[args.skill]]
        else:
            print_error(f"Unknown skill: {args.skill}")
            print_info(f"Available skills: {', '.join(SKILLS.keys())}")
            sys.exit(1)
    else:
        skills_to_check = list(SKILLS.values())
    
    # Check dependencies
    print_header("Checking Dependencies")
    
    checked_skills = []
    for skill in skills_to_check:
        checked_skill = check_skill(skill, system)
        checked_skills.append(checked_skill)
        print_skill_status(checked_skill)
    
    # Print summary
    print_header("Summary")
    
    total_deps = sum(len(s.dependencies) for s in checked_skills)
    satisfied_deps = sum(
        1 for s in checked_skills for d in s.dependencies if d.installed
    )
    missing_required = [
        d for s in checked_skills for d in s.dependencies
        if not d.installed and not d.optional
    ]
    
    print(f"  {Colors.BOLD}Total Dependencies:{Colors.RESET} {total_deps}")
    print(f"  {Colors.BOLD}Satisfied:{Colors.RESET} {Colors.GREEN}{satisfied_deps}{Colors.RESET}")
    
    if missing_required:
        print(f"  {Colors.BOLD}Missing (Required):{Colors.RESET} {Colors.RED}{len(missing_required)}{Colors.RESET}")
        for dep in missing_required:
            cmd = get_install_command(dep, system)
            print(f"    {Colors.RED}• {dep.name}{Colors.RESET}")
            if cmd:
                print(f"      {Colors.DIM}Install: {cmd}{Colors.RESET}")
    
    # Generate report if requested
    if args.report:
        report = generate_report(checked_skills, system)
        report_path = Path("dependency-report.json")
        report_path.write_text(json.dumps(report, indent=2))
        print_info(f"Report saved to {report_path}")
    
    # Auto-install if requested
    if args.install or args.dry_run:
        if missing_required:
            print_header("Installing Missing Dependencies")
            
            success_count = 0
            for dep in missing_required:
                if install_dependency(dep, system, dry_run=args.dry_run):
                    success_count += 1
            
            if args.dry_run:
                print_info(f"[dry-run] Would install {len(missing_required)} dependencies")
            else:
                print_info(f"Successfully installed {success_count}/{len(missing_required)} dependencies")
        else:
            print_success("All required dependencies are satisfied!")
    
    # Exit with error code if missing required dependencies
    if missing_required and not (args.install or args.dry_run):
        sys.exit(1)
    
    sys.exit(0)


if __name__ == "__main__":
    main()