RULES = {
    "Images": [
        ".png", ".jpg", ".jpeg", ".jpe", ".jfif", ".pjpeg", ".pjp",
        ".gif", ".bmp", ".dib", ".tif", ".tiff", ".webp", ".svg",
        ".svgz", ".ico", ".heic", ".heif", ".avif", ".apng",
        ".psd", ".ai", ".eps", ".raw", ".cr2", ".cr3", ".nef",
        ".arw", ".orf", ".rw2", ".dng", ".xcf", ".kra", ".dds",
        ".exr", ".hdr", ".ppm", ".pgm", ".pbm", ".pnm", ".tga",
        ".icns", ".jp2", ".j2k", ".jxr"
    ],

    "Videos": [
        ".mp4", ".m4v", ".mkv", ".avi", ".mov", ".wmv", ".flv",
        ".webm", ".mpeg", ".mpg", ".mpe", ".3gp", ".3g2", ".ts",
        ".mts", ".m2ts", ".vob", ".ogv", ".rm", ".rmvb", ".asf",
        ".f4v", ".divx", ".amv", ".mxf", ".nut", ".y4m"
    ],

    "Audio": [
        ".mp3", ".wav", ".flac", ".aac", ".m4a", ".ogg", ".oga",
        ".opus", ".wma", ".aiff", ".aif", ".mid", ".midi", ".amr",
        ".ac3", ".ape", ".wv", ".pcm", ".ra", ".tta", ".caf",
        ".au", ".snd", ".mka", ".dsf", ".dff"
    ],

    "Documents": [
        ".pdf", ".txt", ".rtf", ".doc", ".docx", ".docm",
        ".odt", ".ods", ".odp", ".ott", ".csv", ".tsv",
        ".xls", ".xlsx", ".xlsm", ".ppt", ".pptx", ".pptm",
        ".pages", ".numbers", ".key", ".epub", ".mobi",
        ".azw", ".azw3", ".md", ".markdown", ".tex",
        ".texi", ".rst", ".log", ".ini", ".cfg", ".conf",
        ".yaml", ".yml", ".toml", ".json", ".xml"
    ],

    "Archives": [
        ".zip", ".zipx", ".7z", ".rar", ".tar", ".gz",
        ".gzip", ".bz2", ".xz", ".lz", ".lz4", ".zst",
        ".cab", ".arj", ".cpio", ".deb", ".rpm", ".pkg",
        ".apk", ".ipa", ".jar", ".war", ".ear", ".iso",
        ".img", ".dmg", ".toast", ".tgz", ".tbz2", ".txz"
    ],

    "Code": [
        # Python
        ".py", ".pyw", ".pyi",

        # Web
        ".html", ".htm", ".css", ".scss", ".sass", ".less",
        ".js", ".jsx", ".ts", ".tsx",

        # C/C++
        ".c", ".h", ".cpp", ".cc", ".cxx", ".hpp", ".hh", ".hxx",

        # C#
        ".cs",

        # Java/Kotlin
        ".java", ".kt", ".kts",

        # Swift / Apple
        ".swift", ".m", ".mm",

        # Rust / Go / Zig
        ".rs", ".go", ".zig",

        # Lua
        ".lua",

        # Ruby / PHP / Perl
        ".rb", ".php", ".pl", ".pm",

        # Shell
        ".sh", ".bash", ".zsh", ".fish",

        # Other languages
        ".r", ".jl", ".nim", ".dart", ".scala",
        ".groovy", ".erl", ".hrl", ".ex", ".exs",
        ".clj", ".cljs", ".fs", ".fsi", ".f90",
        ".f95", ".for", ".asm", ".s", ".v",
        ".vh", ".sv", ".vhd", ".sql", ".ps1",
        ".psm1", ".bat", ".cmd", ".awk", ".sed",

        # Config / Build
        ".cmake", ".gradle", ".make", ".mk",
        ".dockerfile", ".tf", ".tfvars"
    ],

    "Executables": [
        # Windows
        ".exe", ".msi", ".com", ".scr", ".dll",

        # Linux
        ".AppImage", ".run", ".bin", ".deb", ".rpm",

        # macOS
        ".app", ".dmg", ".pkg",

        # Scripts
        ".sh", ".bash", ".zsh", ".fish",
        ".bat", ".cmd", ".ps1", ".vbs",

        # Java
        ".jar"
    ],

    "Fonts": [
        ".ttf", ".otf", ".ttc", ".woff", ".woff2",
        ".eot", ".pfb", ".pfm", ".fon", ".fnt"
    ],

    "Disk Images": [
        ".iso", ".img", ".dmg", ".vhd", ".vhdx",
        ".vdi", ".vmdk", ".qcow", ".qcow2"
    ],

    "Databases": [
        ".db", ".sqlite", ".sqlite3", ".mdb",
        ".accdb", ".sql", ".db3", ".frm",
        ".myd", ".myi"
    ],

    "Virtual Machines": [
        ".ova", ".ovf", ".vmdk", ".vdi",
        ".vhd", ".vhdx", ".qcow", ".qcow2"
    ],

    "3D Models": [
        ".obj", ".fbx", ".blend", ".stl",
        ".dae", ".3ds", ".gltf", ".glb",
        ".ply", ".usd", ".usdz", ".x3d"
    ],

    "CAD": [
        ".dwg", ".dxf", ".step", ".stp",
        ".iges", ".igs", ".sldprt", ".sldasm"
    ],

    "eBooks": [
        ".epub", ".mobi", ".azw", ".azw3",
        ".fb2", ".cbz", ".cbr"
    ],

    "Torrent": [
        ".torrent"
    ],

    "Certificates": [
        ".pem", ".crt", ".cer", ".csr",
        ".key", ".p12", ".pfx", ".der"
    ],

    "Subtitles": [
        ".srt", ".ass", ".ssa", ".vtt",
        ".sub", ".idx"
    ],

    "Game Files": [
        ".sav", ".pak", ".wad", ".bsp",
        ".unitypackage", ".blend", ".rom",
        ".nes", ".gba", ".gb", ".gbc",
        ".nds", ".3ds", ".cia", ".iso"
    ]
}



def get_folder_for(extension: str) -> str:
    ext = extension.lower()
    for folder, extensions in RULES.items():
        if ext in extensions:
            return folder
    return "Misc"  # unknown extensions go here 