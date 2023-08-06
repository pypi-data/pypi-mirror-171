import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

import { IThemeManager } from '@jupyterlab/apputils';
import { ISettingRegistry } from '@jupyterlab/settingregistry';
import Jijsplash from './splash';
import { jupyterFaviconIcon, jupyterIcon } from '@jupyterlab/ui-components';
import logoSvg from '../style/images/jijzept.svg';
/**
 * Initialization data for the jijzeptlab_themes extension.
 */
const themes: JupyterFrontEndPlugin<void> = {
  id: 'jijzeptlab_themes:plugin',
  autoStart: true,
  requires: [IThemeManager, ISettingRegistry],
  activate: (
    app: JupyterFrontEnd,
    manager: IThemeManager,
    settingRegistry: ISettingRegistry
  ) => {
    const style = 'jijzeptlab_themes/index.css';
    jupyterFaviconIcon.svgstr = logoSvg;
    jupyterIcon.svgstr = logoSvg;

    let width = '';
    // Load settings
    Promise.all([settingRegistry.load(themes.id), app.restored]).then(
      async ([settings]) => {
        width = settings.get('maxCellWidth').composite as string;
        document.documentElement.style.setProperty('--max-cell-width', width);
      }
    );
    manager.register({
      name: 'JijZeptLab Light Theme',
      isLight: true,
      load: () => {
        // Theme colors
        document.documentElement.style.setProperty(
          '--tailwind-layout-color0',
          'rgb(var(--tailwind-white))'
        );
        document.documentElement.style.setProperty(
          '--tailwind-layout-color1',
          'rgb(var(--tailwind-white))'
        );
        document.documentElement.style.setProperty(
          '--tailwind-layout-color2',
          'var(--tailwind-grey-300)'
        );
        document.documentElement.style.setProperty(
          '--tailwind-layout-color3',
          'var(--tailwind-indigo-600)'
        );
        document.documentElement.style.setProperty(
          '--tailwind-layout-color4',
          'var(--tailwind-grey-600)'
        );

        document.documentElement.style.setProperty(
          '--tailwind-inverse-layout-color2',
          'var(--tailwind-grey-400)'
        );
        // document.documentElement.style.setProperty(
        //   '--tailwind-inverse-layout-color3',
        //   'var(--tailwind-indigo-800)'
        // );
        document.documentElement.style.setProperty(
          '--tailwind-inverse-layout-color3',
          'var(--tailwind-blue-800)'
        );
        // Object & font colors
        document.documentElement.style.setProperty(
          '--tailwind-background-color',
          'var(--tailwind-grey-100)'
        );
        document.documentElement.style.setProperty(
          '--tailwind-code-cell-color',
          'var(--md-grey-100)'
        );
        document.documentElement.style.setProperty(
          '--tailwind-base-font-color',
          'var(--tailwind-black)'
        );
        document.documentElement.style.setProperty(
          '--tailwind-inverse-font-color',
          'var(--tailwind-white)'
        );
        document.documentElement.style.setProperty(
          '--jp-rendermime-error-background',
          'var(--tailwind-red-200)'
        );

        // Menu color
        // document.documentElement.style.setProperty(
        //   '--tailwind-menu-color',
        //   'var(--tailwind-indigo-800)'
        // );
        document.documentElement.style.setProperty(
          '--tailwind-menu-color',
          'var(--jijzept-main-bule)'
        );

        // Line border color
        document.documentElement.style.setProperty(
          '--jp-border-color2',
          'var(--tailwind-grey-400)'
        );

        // Editor colors
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-keyword-color',
          'var(--tailwind-green-700)'
        );
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-atom-color',
          'var(--tailwind-blue-600)'
        );
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-number-color',
          '#080'
        );
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-def-color',
          '#00f'
        );
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-variable-color',
          'var(--jp-content-font-color1)'
        );
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-variable-2-color',
          'var(--tailwind-blue-600)'
        );
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-variable-3-color',
          'var(--tailwind-green-600)'
        );
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-punctuation-color',
          'var(--tailwind-blue-600)'
        );
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-property-color',
          'var(--tailwind-blue-600)'
        );
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-operator-color',
          '#aa22ff'
        );
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-comment-color',
          '#408080'
        );
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-string-color',
          '#ba2121'
        );
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-string-2-color',
          '#708'
        );
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-meta-color',
          '#aa22ff'
        );
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-qualifier-color',
          '#555'
        );
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-builtin-color',
          'var(--tailwind-green-700)'
        );
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-bracket-color',
          '#997'
        );
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-tag-color',
          'var(--tailwind-green-700)'
        );
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-attribute-color',
          'var(--tailwind-blue-700)'
        );
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-header-color',
          'var(--tailwind-blue-500)'
        );
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-quote-color',
          'var(--tailwind-green-700)'
        );
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-link-color',
          'var(--tailwind-blue-700)'
        );
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-error-color',
          '#f00'
        );
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-hr-color',
          '#999'
        );
        document.documentElement.style.setProperty(
          '--jp-notebook-multiselected-color',
          'var(--tailwind-blue-100)'
        );

        // Search result highlighting
        document.documentElement.style.setProperty(
          '--jp-search-selected-match-background-color',
          'var(--tailwind-green-400)'
        );
        document.documentElement.style.setProperty(
          '--jp-search-unselected-match-background-color',
          'var(--tailwind-green-200)'
        );

        // Scrollbar color
        document.documentElement.style.setProperty(
          '--tailwind-scrollbar-thumb-color',
          'var(--tailwind-grey-400)'
        );

        document.documentElement.style.setProperty(
          '--jp-statusbar-fontcolor',
          'var(--tailwind-black)'
        );

        return manager.loadCSS(style);
      },
      unload: () => Promise.resolve(undefined)
    });
    manager.register({
      name: 'JijZeptLab Dark Theme',
      isLight: false,
      load: () => {
        // Theme colors
        document.documentElement.style.setProperty(
          '--tailwind-layout-color0',
          'var(--tailwind-grey-900)'
        );
        document.documentElement.style.setProperty(
          '--tailwind-layout-color1',
          'var(--tailwind-grey-900)'
        );
        document.documentElement.style.setProperty(
          '--tailwind-layout-color2',
          'var(--tailwind-grey-950)'
        );
        document.documentElement.style.setProperty(
          '--tailwind-layout-color3',
          'var(--tailwind-indigo-300)'
        );
        document.documentElement.style.setProperty(
          '--tailwind-layout-color4',
          'var(--tailwind-grey-400)'
        );

        document.documentElement.style.setProperty(
          '--tailwind-inverse-layout-color2',
          'var(--tailwind-grey-600)'
        );
        // document.documentElement.style.setProperty(
        //   '--tailwind-inverse-layout-color3',
        //   'var(--tailwind-indigo-600)'
        // );

        document.documentElement.style.setProperty(
          '--tailwind-inverse-layout-color3',
          'var(--tailwind-blue-600)'
        );

        // Object & font colors
        document.documentElement.style.setProperty(
          '--tailwind-background-color',
          'rgb(var(--tailwind-black))'
        );
        document.documentElement.style.setProperty(
          '--tailwind-code-cell-color',
          'var(--tailwind-grey-800)'
        );
        document.documentElement.style.setProperty(
          '--tailwind-base-font-color',
          'var(--tailwind-white)'
        );
        document.documentElement.style.setProperty(
          '--tailwind-inverse-font-color',
          'var(--tailwind-black)'
        );
        document.documentElement.style.setProperty(
          '--jp-rendermime-error-background',
          'var(--tailwind-red-900)'
        );

        // Menu color
        // document.documentElement.style.setProperty(
        //   '--tailwind-menu-color',
        //   'var(--tailwind-indigo-800)'
        // );
        document.documentElement.style.setProperty(
          '--tailwind-menu-color',
          'var(--jijzept-main-bule)'
        );

        // Line border color
        document.documentElement.style.setProperty(
          '--jp-border-color2',
          'var(--tailwind-grey-700)'
        );

        // Editor colors
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-keyword-color',
          'var(--tailwind-green-500)'
        );
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-atom-color',
          'var(--tailwind-blue-300)'
        );
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-number-color',
          '#b5cea8'
        );
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-def-color',
          '#79d9ff'
        );
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-variable-color',
          'var(--jp-content-font-color1)'
        );
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-variable-2-color',
          '#79d9ff'
        );
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-variable-3-color',
          'var(--tailwind-green-600)'
        );
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-punctuation-color',
          '#79d9ff'
        );
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-property-color',
          '#79d9ff'
        );
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-operator-color',
          '#daabf7'
        );
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-comment-color',
          '#aebca8'
        );
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-string-color',
          '#ce9178'
        );
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-string-2-color',
          'var(--tailwind-purple-300)'
        );
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-meta-color',
          '#daabf7'
        );
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-qualifier-color',
          '#555'
        );
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-builtin-color',
          'var(--tailwind-green-600)'
        );
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-bracket-color',
          '#997'
        );
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-tag-color',
          'var(--tailwind-green-700)'
        );
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-attribute-color',
          'var(--tailwind-blue-700)'
        );
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-header-color',
          'var(--tailwind-blue-500)'
        );
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-quote-color',
          'var(--tailwind-green-300)'
        );
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-link-color',
          'var(--tailwind-blue-700)'
        );
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-error-color',
          '#f00'
        );
        document.documentElement.style.setProperty(
          '--jp-mirror-editor-hr-color',
          '#999'
        );
        document.documentElement.style.setProperty(
          '--jp-notebook-multiselected-color',
          'var(--tailwind-blue-900)'
        );

        // Search result highlighting
        document.documentElement.style.setProperty(
          '--jp-search-selected-match-background-color',
          'var(--tailwind-green-600)'
        );
        document.documentElement.style.setProperty(
          '--jp-search-unselected-match-background-color',
          'var(--tailwind-green-800)'
        );

        // Scrollbar color
        document.documentElement.style.setProperty(
          '--tailwind-scrollbar-thumb-color',
          'var(--tailwind-grey-700)'
        );

        document.documentElement.style.setProperty(
          '--jp-statusbar-fontcolor',
          'var(--tailwind-white)'
        );
        return manager.loadCSS(style);
      },
      unload: () => Promise.resolve(undefined)
    });
  }
};

const plugin: JupyterFrontEndPlugin<any>[] = [themes, Jijsplash];

export default plugin;
