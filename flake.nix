{
  description = "Chip Music Tool Flake";

  inputs.nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";

  outputs = {
    self,
    nixpkgs,
    ...
  }: let
    system = "x86_64-linux";
    pythonVersion = "3.10.1";
    pkgs = import nixpkgs {inherit system;};
    profile = "python";
  in {
    devShells.${system}.default = pkgs.mkShell {
      packages = with pkgs; [
        alejandra
        statix
        deadnix
        nil
        nixd
        (python3.withPackages (ps: with ps; [pygame]))
      ];

      shellHook = ''
        export VSCODE_PROFILE="${profile}";
      '';
    };
  };
}
