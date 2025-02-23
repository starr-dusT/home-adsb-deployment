with (import <nixpkgs> {});

pkgs.mkShellNoCC {
  packages = with pkgs; [
    netcat
  ];
  buildInputs = with pkgs.python3Packages; [
    python
    venvShellHook
    pandas
    numpy
    matplotlib
  ];
  venvDir = "./.venv";
  postVenvCreation = ''
    unset SOURCE_DATE_EPOCH
  '';
  postShellHook = ''
    unset SOURCE_DATE_EPOCH
  '';
}
